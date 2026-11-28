"""Gates for the goals area filter — baseline docs/SCOPE_GOALS_AREA_FILTER.md.

The defect these answer (owner report 2026-11-28): every gate showed the same
unfiltered list, so whatever gate you walked through you saw the first goal,
which was a Mental one. `life_area` was written on save and never read back.

These tests RUN the logic. The test they replace matched the string
`_zz_prefill_goal_area` in the source and never executed a line, which is why
a green bar said nothing about this behaviour (Law 5: the gate is the
deliverable). Acceptance A7: delete the WHERE clause and this suite goes red.

Run from the repo root:   python -m unittest discover -s tests
"""
import ast
import os
import unittest

from lyceum import goals
from lyceum.db import study_db

_REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_APP = os.path.join(_REPO, "sentinel_personal_development.py")

_NOW = "2026-11-28T00:00:00"


def _add_goal(title, area):
    return study_db.db_exec(
        "INSERT INTO goals (title, life_area, created_at, updated_at) "
        "VALUES (?,?,?,?)", (title, area, _NOW, _NOW))


class ListQueryTest(unittest.TestCase):
    """ALGORITHM GoalsListQuery, line by line."""

    def test_an_area_adds_a_bound_where_clause(self):
        sql, params = goals.list_query("physical")
        self.assertIn("WHERE life_area = ?", sql)
        self.assertEqual(params, ("physical",))

    def test_the_key_is_bound_never_interpolated(self):
        sql, _ = goals.list_query("financial")
        self.assertNotIn("financial", sql,
                         "the area key reached the SQL text — bind it")

    def test_no_area_means_every_area(self):
        sql, params = goals.list_query()
        self.assertNotIn("WHERE", sql)
        self.assertEqual(params, ())

    def test_an_unknown_area_fails_loudly(self):
        """A typo must raise, not quietly render an empty room."""
        with self.assertRaises(ValueError):
            goals.list_query("mentl")

    def test_the_order_is_unchanged(self):
        for sql in (goals.list_query()[0], goals.list_query("career")[0]):
            self.assertIn("ORDER BY (status='done'), id DESC", sql)


class EmptyStateTest(unittest.TestCase):
    """ALGORITHM EmptyStateLine — an empty box is a mystery, a sentence is not."""

    def test_an_empty_gate_says_which_gate(self):
        line = goals.empty_state_line("physical")
        self.assertIn("physical", line)
        self.assertIn("Save", line)

    def test_every_area_has_its_own_wording(self):
        self.assertTrue(goals.empty_state_line().strip())
        self.assertNotIn("gate", goals.empty_state_line())


class RoundTripTest(unittest.TestCase):
    """Acceptance A1, proven against a real table in a throwaway database."""

    def test_each_gate_sees_only_its_own_goals(self):
        with study_db.temp_study_db():
            study_db.init_study_db()
            _add_goal("read other people", "mental")
            _add_goal("walk every morning", "physical")
            _add_goal("pay off the truck", "financial")
            _add_goal("second mental one", "mental")

            for area, expected in (("mental", 2), ("physical", 1),
                                   ("financial", 1), ("social", 0)):
                rows = study_db.db_query(*goals.list_query(area))
                self.assertEqual(len(rows), expected, "area %r" % (area,))
                for row in rows:
                    self.assertEqual(row[-1], area,
                                     "a goal from another area leaked in")

    def test_no_area_still_shows_everything(self):
        with study_db.temp_study_db():
            study_db.init_study_db()
            _add_goal("one", "mental")
            _add_goal("two", "career")
            self.assertEqual(len(study_db.db_query(*goals.list_query())), 2)


class AreaKeysMatchTheAppTest(unittest.TestCase):
    """Static gate (Law 5): the pure keys and the wheel's keys cannot drift."""

    def test_wheel_areas_match_the_pure_area_keys(self):
        with open(_APP, encoding="utf-8") as f:
            tree = ast.parse(f.read())
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign) and any(
                    isinstance(t, ast.Name) and t.id == "_WHEEL_AREAS"
                    for t in node.targets):
                wheel = tuple(k for k, _lab in ast.literal_eval(node.value))
                break
        else:
            self.fail("_WHEEL_AREAS not found in the app source")
        self.assertEqual(wheel, goals.AREA_KEYS,
                         "the wheel's area keys and lyceum.goals.AREA_KEYS "
                         "have drifted apart")


if __name__ == "__main__":
    unittest.main()
