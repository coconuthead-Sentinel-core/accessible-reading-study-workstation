# SENTINEL'S FORGE · Board — Goals Area Filter

Stage 2 (Design) under `classroom-code`. Baseline:
`docs/SCOPE_GOALS_AREA_FILTER.md`, BASELINED 2026-11-28.
Not code. Reviewed line by line before any Python is written.

**Stage 1 (Requirements), one sentence per in-scope item:**

1. The goals list shows only the goals of the gate you walked through.
2. Every door into the Goals room lands on a defined state.
3. Every decline on that path writes a breadcrumb and says so on screen.
4. The goals list stops sharing its selection with other widgets.
5. A test that runs the filter fails if the filter is removed.

```text
ALGORITHM GoalsListQuery
INPUT:  area — a life-area key, or NOTHING for "every area"
OUTPUT: (sql, params) — the list query and the values bound to it
INVARIANT: area is NEVER pasted into the sql text, only bound

1. columns ← "id, title, progress, status, target_date, created_at, life_area"
2. order   ← "ORDER BY (status='done'), id DESC"
3. IF area = NOTHING
    3.1 RETURN ("SELECT " + columns + " FROM goals " + order, ())
4. ASSERT area is one of the seven known area keys   // ✓ a typo must not quietly empty the room
5. RETURN ("SELECT " + columns + " FROM goals WHERE life_area = ? " + order, (area,))


ALGORITHM EmptyStateLine
INPUT:  area_label — the gate's display label, or NOTHING
OUTPUT: one sentence to stand where the list would be

1. IF area_label = NOTHING
    1.1 RETURN "No goals yet. Name one above, then Save."
2. RETURN "No goals behind the " + area_label + " gate yet. Name one above, then Save."


ALGORITHM EnterGoalsRoom                 // the ONE door — every button calls this
INPUT:  area — a life-area key, or NOTHING for "every area"
OUTPUT: none; the Goals room is on screen in a DEFINED state
POSTCONDITION: the form holds no goal id, and the badge names `area`

1. CALL show_goals_screen()
2. IF the goals room was never built
    2.1 CALL breadcrumb("goals-enter: DECLINED — room not built")
    2.2 CALL set_status("The Goals room did not open. Say the word and I'll look.")
    2.3 STOP → owner decides              // never a silent pass
3. CALL clear_form()                      // goal id ← NOTHING, every field blank
4. view_area ← area
5. IF area ≠ NOTHING
    5.1 badge ← CALL label_for(area)
6. CALL RefreshGoalsList(view_area)
7. CALL focus(goal_title_field)
8. CALL breadcrumb("goals-enter: area=" + area + " rows=" + count + " form=cleared")
9. ASSERT form.goal_id = NOTHING          // ✓ Save must INSERT, never UPDATE
10. ASSERT badge names area               // ✓ settles the one open question


ALGORITHM RefreshGoalsList
INPUT:  area — the area in view, or NOTHING
OUTPUT: none; the list shows exactly the goals of `area`

1. (sql, params) ← CALL GoalsListQuery(area)
2. rows ← CALL database_query(sql, params)
3. CALL list.clear()
4. FOR EACH row IN rows
    4.1 badge ← CALL accountability(row)  // existing pure logic, unchanged
    4.2 CALL list.append(badge + " · " + row.title)
5. IF rows is empty
    5.1 CALL list.show_message(CALL EmptyStateLine(CALL label_for(area)))
6. CALL header.set("Showing: " + (CALL label_for(area) OR "every area"))
7. ASSERT every row shown has life_area = area   // ✓ A1's proof obligation


ALGORITHM WireTheDoors
OUTPUT: none; exactly one way into the Goals room

1. FOR EACH of the seven named gates
    1.1 button.command ← CALL EnterGoalsRoom(that gate's area key)
2. purple "Set goals on weak areas".command ← CALL EnterGoalsRoom(NOTHING)
3. goals_listbox.exportselection ← FALSE         // Law 6 item 1
4. ASSERT no other code path shows the goals room // ✓ one door — Law 4 contract
```

## Where each piece lives (Stage 3 plan, not yet built)

| Piece | Home | Why |
| --- | --- | --- |
| `GoalsListQuery`, `EmptyStateLine` | `lyceum/goals.py` | pure, no Tk, no DB — unit-testable, matches the module already there |
| `EnterGoalsRoom`, `RefreshGoalsList` | `sentinel_personal_development.py` | imperative shell; calls the pure core |
| `WireTheDoors` | `_build_wheel_panel` | replaces two ad-hoc doors with one contract |
| the tests | `tests/test_goals_area_filter.py` | runs against a temp fixture DB, never live data |

No schema change: `life_area` exists, is populated, and `idx_goals_area`
is already on it. No new dependency.
