"""Pure goal-accountability logic, extracted from the BookReader God Object (Q3).

The "cold honest status" decision tree for a goal, plus the list summary — no
Tkinter, no DB. Fully unit-testable across every branch (inject ``today`` for
determinism). The GUI maps the returned semantic ``level`` to a colour, keeping
presentation out of the logic.
"""
from __future__ import annotations

from datetime import date, datetime

LEVELS = ("done", "parked", "no_date", "overdue", "behind", "on_track")


def _parse_date(s):
    try:
        return datetime.strptime((s or "")[:10], "%Y-%m-%d").date()
    except Exception:
        return None


def accountability(created_at, target_date, progress, status, today=None):
    """Return (badge, level, is_behind) for a goal.

    Pace = actual progress vs the share of time elapsed toward the target date;
    falling >10 points behind that pace is BEHIND, a passed date is OVERDUE.
    ``level`` is one of LEVELS. Pure — pass a ``today`` date for deterministic
    tests; defaults to date.today().
    """
    today = today or date.today()
    prog = int(progress or 0)
    st = (status or "active").lower()
    if st == "done" or prog >= 100:
        return ("✅ DONE", "done", False)
    if st == "parked":
        return ("⏸ PARKED", "parked", False)
    tgt = _parse_date(target_date)
    started = _parse_date(created_at) or today
    if tgt is None:
        return ("• SET A DATE", "no_date", False)
    if tgt < today:
        return (f"⛔ OVERDUE {(today - tgt).days}d", "overdue", True)
    span = max(1, (tgt - started).days)
    elapsed = max(0, (today - started).days)
    expected = min(100, int(100 * elapsed / span))
    if prog < expected - 10:
        return (f"🔻 BEHIND {prog}/{expected}%", "behind", True)
    return (f"🟢 ON TRACK {(tgt - today).days}d", "on_track", False)


def summarize(rows, today=None):
    """Classify many goals at once.

    ``rows``: iterable of (created_at, target_date, progress, status). Returns
    (per, (n_behind, n_ok, n_done)) where per[i] = (badge, level, is_behind),
    aligned with the input order. Pure.
    """
    today = today or date.today()
    per = []
    n_bad = n_ok = n_done = 0
    for created, target, prog, status in rows:
        badge, level, behind = accountability(created, target, prog, status, today)
        per.append((badge, level, behind))
        if behind:
            n_bad += 1
        elif level == "done":
            n_done += 1
        else:
            n_ok += 1
    return per, (n_bad, n_ok, n_done)


# ---------------------------------------------------------------------------
# Area filtering — baseline: docs/SCOPE_GOALS_AREA_FILTER.md (2026-11-28),
# blueprint: docs/BLUEPRINT_GOALS_AREA_FILTER.md (ALGORITHM GoalsListQuery,
# ALGORITHM EmptyStateLine). Pure: no Tkinter, no DB handle, no I/O.
# ---------------------------------------------------------------------------

#: The seven life areas, in wheel order. The GUI's ``_WHEEL_AREAS`` keys must
#: match this tuple exactly; ``tests/test_goals_area_filter.py`` gates it so the
#: two cannot drift apart silently.
AREA_KEYS = ("mental", "spiritual", "physical", "family",
             "financial", "career", "social")

_LIST_COLUMNS = "id, title, progress, status, target_date, created_at, life_area"
_LIST_ORDER = "ORDER BY (status='done'), id DESC"


def list_query(area=None):
    """Return ``(sql, params)`` for the goals list, filtered to one life area.

    ``area`` is a key from :data:`AREA_KEYS`, or ``None`` for every area. The
    key is always BOUND as a parameter, never interpolated into the SQL text.

    Raises ``ValueError`` on an unknown key: a typo must fail loudly rather
    than quietly render an empty room, which is the defect this function
    exists to answer (every gate showed the same unfiltered list).
    """
    if area is None:
        return ("SELECT %s FROM goals %s" % (_LIST_COLUMNS, _LIST_ORDER), ())
    if area not in AREA_KEYS:
        raise ValueError("unknown life area: %r" % (area,))
    return ("SELECT %s FROM goals WHERE life_area = ? %s"
            % (_LIST_COLUMNS, _LIST_ORDER), (area,))


def empty_state_line(area_label=None):
    """The sentence that stands where the list would be when it is empty.

    ``area_label`` is the gate's display label (e.g. "physical"), or ``None``
    when every area is in view. An empty box is a mystery; a sentence is not.
    """
    if not area_label:
        return "No goals yet. Name one above, then Save."
    return ("No goals behind the %s gate yet. Name one above, then Save."
            % (area_label,))
