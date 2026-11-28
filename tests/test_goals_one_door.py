"""Static gates for the ONE door into the Goals room.

Baseline: docs/SCOPE_GOALS_AREA_FILTER.md (BASELINED 2026-11-28), §1 items
2, 3 and 4. Blueprint: ALGORITHM EnterGoalsRoom / ALGORITHM WireTheDoors.

These replace `test_wheel_buttons_wired_to_goals_prefill`, which matched the
string `_zz_prefill_goal_area` in the source and never executed a line. It
was green the whole time two doors reached the panel by different routes and
one of them handed over a stale form (Law 5: the gate is the deliverable).

Run from the repo root:   python -m unittest discover -s tests
"""
import ast
import os
import unittest

_REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_APP = os.path.join(_REPO, "sentinel_personal_development.py")

_TREE = None


def _app_tree():
    global _TREE
    if _TREE is None:
        with open(_APP, encoding="utf-8") as f:
            _TREE = ast.parse(f.read())
    return _TREE


def _func(name):
    for node in ast.walk(_app_tree()):
        if isinstance(node, ast.FunctionDef) and node.name == name:
            return node
    raise AssertionError("%s not found in the app source" % name)


def _strings(node):
    return {n.value for n in ast.walk(node)
            if isinstance(n, ast.Constant) and isinstance(n.value, str)}


def _attrs(node):
    return {n.attr for n in ast.walk(node) if isinstance(n, ast.Attribute)}


class OneDoorTest(unittest.TestCase):
    def test_the_goals_panel_registers_the_one_door(self):
        goals_panel = _func("_build_goals_panel")
        registered = any(
            isinstance(n, ast.Assign)
            and any(isinstance(t, ast.Attribute)
                    and t.attr == "_zz_enter_goals_room" for t in n.targets)
            for n in ast.walk(goals_panel))
        self.assertTrue(registered,
                        "_build_goals_panel no longer registers the single "
                        "entry point _zz_enter_goals_room")

    def test_the_gates_reach_the_goals_room_through_it(self):
        # The wheel panel is built BEFORE the goals panel, so it reaches
        # the door late-bound via getattr — the name shows up as a
        # string, not as an attribute access.
        wheel = _func("_build_wheel_panel")
        self.assertIn("_zz_enter_goals_room", _strings(wheel) | _attrs(wheel),
                      "the gate buttons no longer reach the one door")

    def test_the_old_prefill_hook_is_gone(self):
        with open(_APP, encoding="utf-8") as f:
            src = f.read()
        self.assertNotIn("_zz_prefill_goal_area", src,
                         "the replaced prefill hook is back — two names for "
                         "one door is how the second door drifted")

    def test_no_button_is_wired_straight_to_the_screen_switch(self):
        """The weak-areas button used to be `command=goto_goals`, which
        showed the panel without clearing it — you landed on the previous
        goal, still carrying its row id, and Save then UPDATEd it."""
        wheel = _func("_build_wheel_panel")
        for node in ast.walk(wheel):
            if not isinstance(node, ast.Call):
                continue
            for kw in node.keywords:
                if kw.arg == "command" and isinstance(kw.value, ast.Name) \
                        and kw.value.id == "goto_goals":
                    self.fail("a button is wired straight to goto_goals — "
                              "every door must go through EnterGoalsRoom")


class SpeaksWhenItDeclinesTest(unittest.TestCase):
    """Law 3: a handler that declines to act must breadcrumb AND tell."""

    def test_the_gate_path_breadcrumbs(self):
        for fn in ("_build_wheel_panel", "_build_goals_panel"):
            said = [s for s in _strings(_func(fn)) if "goals-enter" in s]
            self.assertTrue(said, "%s writes no goals-enter breadcrumb" % fn)

    def test_every_decline_says_so_on_screen(self):
        for fn in ("_build_wheel_panel", "_build_goals_panel"):
            node = _func(fn)
            self.assertIn("set_status", _attrs(node),
                          "%s declines without telling the owner" % fn)


class ListboxSelectionTest(unittest.TestCase):
    """Law 6 item 1 — a CRUD listbox must not export its selection."""

    def test_goals_listbox_does_not_export_its_selection(self):
        panel = _func("_build_goals_panel")
        for node in ast.walk(panel):
            if not isinstance(node, ast.Call):
                continue
            func = node.func
            if isinstance(func, ast.Attribute) and func.attr == "Listbox":
                for kw in node.keywords:
                    if kw.arg == "exportselection":
                        self.assertIs(kw.value.value, False,
                                      "exportselection must be False")
                        return
                self.fail("the goals Listbox has no exportselection=False — "
                          "Tk's default lets a neighbouring widget steal the "
                          "selection while the form still holds a goal id")
        self.fail("no Listbox found in _build_goals_panel")


if __name__ == "__main__":
    unittest.main()
