"""Unit tests for the note-card grid (lyceum.grid_cards) + schema round-trip.

Pure logic with injected timestamps — no GUI, no clock. Covers the cell
address rule, both traversal orders, neighbours and their gaps, the
next-free search, one-box find, and a temp_study_db round-trip of the
additive grid_cards table.

Every database test goes through ``study_db.temp_study_db()``. That is
the blessed isolation and not a style preference: patching a legacy
``DB_PATH`` while leaving ``STUDY_DB`` alone is exactly what leaked test
rows into the real study.db twice.

Run from the repo root:   python -m unittest discover -s tests
"""
import unittest

from lyceum import grid_cards as gc
from lyceum import util
from lyceum.db import study_db

WHEN = "2026-11-27T09:00:00"


def card(cell, title="t", body="", zone=None, load=None):
    return gc.new_card(cell, title, body, WHEN, zone=zone, load=load)


class AddressTest(unittest.TestCase):
    def test_a_plain_address_parses(self):
        self.assertEqual(gc.parse_cell("H5"), ("H", 5))
        self.assertEqual(gc.parse_cell("Z999"), ("Z", 999))

    def test_dictation_capitalisation_does_not_matter(self):
        # This app is driven by voice; a speech engine capitalises
        # inconsistently and the owner should never have to care.
        self.assertEqual(gc.parse_cell("h5"), ("H", 5))
        self.assertEqual(gc.parse_cell("  h5  "), ("H", 5))

    def test_what_is_not_an_address(self):
        for bad in ("", None, "H", "5", "H0", "AA1", "H1000", "box model"):
            with self.subTest(text=repr(bad)):
                self.assertIsNone(gc.parse_cell(bad))

    def test_formatting_round_trips(self):
        self.assertEqual(gc.parse_cell(gc.format_cell("q", 42)), ("Q", 42))

    def test_is_cell_forks_the_search_box(self):
        self.assertTrue(gc.is_cell("H5"))
        self.assertFalse(gc.is_cell("box model"))


class CardTest(unittest.TestCase):
    def test_a_card_round_trips_its_fields(self):
        c = card("H5", "The box model", "padding", zone="YELLOW", load=6)
        self.assertEqual(c["cell"], "H5")
        self.assertEqual(c["zone"], "YELLOW")
        self.assertEqual(c["load"], 6)

    def test_a_missing_title_is_refused(self):
        # str(None) is the truthy string "None" — a card would otherwise
        # be filed literally named None.
        for bad in ("", "   ", None):
            with self.subTest(title=repr(bad)):
                with self.assertRaises(ValueError):
                    card("H5", title=bad)

    def test_a_load_without_a_zone_uses_the_app_wide_mapping(self):
        """One vocabulary across the app, not two.

        A card and an excerpt at the same load must land in the same
        zone, or the word GREEN means two different things inside one
        program.
        """
        for load in (1, 3, 4, 6, 7, 10):
            with self.subTest(load=load):
                self.assertEqual(card("H5", load=load)["zone"],
                                 util.zone_for_load(load))

    def test_an_explicit_zone_wins_over_the_mapping(self):
        self.assertEqual(card("H5", zone="RED", load=10)["zone"], "RED")

    def test_no_load_and_no_zone_defaults_green(self):
        self.assertEqual(card("H5")["zone"], "GREEN")

    def test_an_off_scale_load_is_refused(self):
        for bad in (0, 11, "6", True):
            with self.subTest(load=repr(bad)):
                with self.assertRaises(ValueError):
                    card("H5", load=bad)

    def test_a_bad_zone_is_refused(self):
        with self.assertRaises(ValueError):
            card("H5", zone="BLUE")


class LinkTest(unittest.TestCase):
    def test_a_card_cannot_link_to_itself(self):
        with self.assertRaises(ValueError):
            gc.new_link("H5", "h5", "relates to")

    def test_an_unknown_relation_is_refused(self):
        with self.assertRaises(ValueError):
            gc.new_link("H5", "A1", "vibes with")


class TraversalTest(unittest.TestCase):
    """The owner's two reading directions."""

    def setUp(self):
        self.grid = [card("A1"), card("B1"), card("A2"), card("B2")]

    def test_row_major_reads_across_then_down(self):
        self.assertEqual([c["cell"] for c in gc.walk(self.grid, gc.ROW_MAJOR)],
                         ["A1", "B1", "A2", "B2"])

    def test_column_major_reads_down_then_across(self):
        self.assertEqual(
            [c["cell"] for c in gc.walk(self.grid, gc.COLUMN_MAJOR)],
            ["A1", "A2", "B1", "B2"])

    def test_the_two_orders_really_differ(self):
        # If they ever agree on a non-trivial grid, one is wrong and the
        # feature is pointless.
        a = [c["cell"] for c in gc.walk(self.grid, gc.ROW_MAJOR)]
        b = [c["cell"] for c in gc.walk(self.grid, gc.COLUMN_MAJOR)]
        self.assertNotEqual(a, b)
        self.assertEqual(sorted(a), sorted(b))

    def test_rows_sort_numerically_not_as_text(self):
        # "10" sorts before "9" as text — a grid that puts row 10 above
        # row 9 is wrong in a way that is easy to miss by eye.
        grid = [card("A10"), card("A9"), card("A2")]
        self.assertEqual(
            [c["cell"] for c in gc.walk(grid, gc.COLUMN_MAJOR)],
            ["A2", "A9", "A10"])

    def test_an_unknown_order_is_refused_even_on_an_empty_grid(self):
        # sorted() never calls the key function on an empty list, so the
        # check has to live in walk() or it passes silently until there
        # are cards.
        with self.assertRaises(ValueError):
            gc.walk([], "DIAGONAL")


class NeighbourTest(unittest.TestCase):
    def test_the_four_neighbours_are_found(self):
        grid = [card("B2"), card("B1"), card("B3"), card("A2"), card("C2")]
        n = gc.neighbours(grid, "B2")
        self.assertEqual(n["up"]["cell"], "B1")
        self.assertEqual(n["down"]["cell"], "B3")
        self.assertEqual(n["left"]["cell"], "A2")
        self.assertEqual(n["right"]["cell"], "C2")

    def test_the_gaps_are_reported_too(self):
        n = gc.neighbours([card("A1")], "A1")
        self.assertEqual(set(n), {"up", "down", "left", "right"})
        self.assertIsNone(n["up"])
        self.assertIsNone(n["left"])

    def test_the_edges_do_not_wrap(self):
        n = gc.neighbours([card("A1")], "A1")
        self.assertIsNone(n["left"])
        self.assertIsNone(n["up"])


class NextFreeTest(unittest.TestCase):
    def test_an_empty_grid_starts_at_a1(self):
        self.assertEqual(gc.next_free([]), "A1")

    def test_the_fill_direction_follows_the_reading_order(self):
        self.assertEqual(gc.next_free([card("A1")], gc.ROW_MAJOR), "B1")
        self.assertEqual(gc.next_free([card("A1")], gc.COLUMN_MAJOR), "A2")

    def test_a_gap_is_filled_before_the_end(self):
        self.assertEqual(
            gc.next_free([card("A1"), card("C1")], gc.ROW_MAJOR), "B1")


class FindTest(unittest.TestCase):
    def setUp(self):
        self.grid = [
            card("H5", "The box model", "padding border margin"),
            card("A1", "Flexbox", "a box that flexes"),
            card("B2", "Specificity", "ids beat classes"),
        ]

    def test_an_address_jumps_to_one_card(self):
        hits = gc.find(self.grid, "h5")
        self.assertEqual(len(hits), 1)
        self.assertEqual(hits[0]["title"], "The box model")

    def test_words_search_title_and_body(self):
        self.assertEqual(len(gc.find(self.grid, "box")), 2)

    def test_word_order_does_not_matter(self):
        self.assertEqual([c["cell"] for c in gc.find(self.grid, "box model")],
                         [c["cell"] for c in gc.find(self.grid, "model box")])

    def test_more_matching_words_ranks_higher(self):
        self.assertEqual(gc.find(self.grid, "box model")[0]["cell"], "H5")

    def test_an_empty_query_finds_nothing(self):
        for q in ("", "   ", None, "!!!"):
            with self.subTest(query=repr(q)):
                self.assertEqual(gc.find(self.grid, q), [])


class ValidateTest(unittest.TestCase):
    def test_a_clean_grid_reports_nothing(self):
        grid = [card("A1"), card("B2")]
        self.assertEqual(
            gc.validate(grid, [gc.new_link("A1", "B2", "relates to")]), [])

    def test_a_duplicate_address_is_reported(self):
        self.assertTrue(any("duplicate" in p for p in
                            gc.validate([card("A1"), card("A1")], [])))

    def test_a_link_to_nowhere_is_reported(self):
        problems = gc.validate([card("A1")],
                               [{"src": "A1", "dst": "Q9",
                                 "relation": "relates to"}])
        self.assertTrue(any("names no card" in p for p in problems))


class SchemaRoundTripTest(unittest.TestCase):
    """The additive grid tables, on a throwaway database."""

    def test_the_tables_are_created_without_disturbing_the_others(self):
        with study_db.temp_study_db():
            study_db.init_study_db()
            con = study_db.connect()
            try:
                names = {r[0] for r in con.execute(
                    "SELECT name FROM sqlite_master WHERE type='table'")}
            finally:
                con.close()
            self.assertLessEqual({"grid_cards", "grid_card_links"}, names)
            # The migration is additive: what was already there stays.
            self.assertIn("highlights", names)
            self.assertIn("memory_cards", names)

    def test_a_card_round_trips(self):
        with study_db.temp_study_db():
            study_db.init_study_db()
            study_db.save_grid_card(card("H5", "The box model", "padding",
                                         load=6))
            rows = study_db.grid_cards_all()
            self.assertEqual(len(rows), 1)
            self.assertEqual(rows[0]["cell"], "H5")
            self.assertEqual(rows[0]["load"], 6)

    def test_saving_the_same_address_updates_rather_than_duplicates(self):
        """The address IS the identity.

        Two cards at H5 would make "go to H5" ambiguous, which defeats
        the point of having addresses at all.
        """
        with study_db.temp_study_db():
            study_db.init_study_db()
            study_db.save_grid_card(card("H5", "First try"))
            study_db.save_grid_card(card("H5", "Better title", "with a body"))
            rows = study_db.grid_cards_all()
            self.assertEqual(len(rows), 1)
            self.assertEqual(rows[0]["title"], "Better title")

    def test_a_card_is_fetched_by_address_case_insensitively(self):
        with study_db.temp_study_db():
            study_db.init_study_db()
            study_db.save_grid_card(card("H5", "The box model"))
            self.assertEqual(study_db.grid_card_at("h5")["title"],
                             "The box model")
            self.assertIsNone(study_db.grid_card_at("Q9"))

    def test_the_kernel_reads_stored_rows_unchanged(self):
        """The seam that matters: traversal over rows that made the trip."""
        with study_db.temp_study_db():
            study_db.init_study_db()
            for cell, title in (("A1", "Flexbox"), ("B1", "Grid"),
                                ("A2", "Box model")):
                study_db.save_grid_card(card(cell, title))
            stored = study_db.grid_cards_all()
            self.assertEqual(gc.validate(stored, study_db.grid_links()), [])
            self.assertEqual(
                [c["cell"] for c in gc.walk(stored, gc.ROW_MAJOR)],
                ["A1", "B1", "A2"])
            self.assertEqual(
                [c["cell"] for c in gc.walk(stored, gc.COLUMN_MAJOR)],
                ["A1", "A2", "B1"])

    def test_a_stored_load_comes_back_a_whole_number(self):
        # sqlite is loosely typed; "6" would pass validate and poison
        # every comparison downstream.
        with study_db.temp_study_db():
            study_db.init_study_db()
            study_db.save_grid_card(card("H5", "t", load=6))
            self.assertIsInstance(study_db.grid_cards_all()[0]["load"], int)

    def test_links_can_be_narrowed_to_one_card(self):
        with study_db.temp_study_db():
            study_db.init_study_db()
            for cell in ("A1", "B2", "C3"):
                study_db.save_grid_card(card(cell))
            study_db.save_grid_link(gc.new_link("A1", "B2", "relates to"))
            study_db.save_grid_link(gc.new_link("B2", "C3", "depends on"))
            self.assertEqual(len(study_db.grid_links()), 2)
            self.assertEqual(len(study_db.grid_links("A1")), 1)
            self.assertEqual(len(study_db.grid_links("B2")), 2)

    def test_the_schema_check_constraint_refuses_a_bad_zone(self):
        """Belt and braces: the kernel validates, and so does SQLite.

        The kernel is the first gate, but a row written by any other
        path still has to be legal.
        """
        import sqlite3
        with study_db.temp_study_db():
            study_db.init_study_db()
            with self.assertRaises(sqlite3.IntegrityError):
                study_db.db_exec(
                    "INSERT INTO grid_cards (cell, title, zone, created_at) "
                    "VALUES ('Z9', 't', 'BLUE', ?)", (WHEN,))


if __name__ == "__main__":
    unittest.main()
