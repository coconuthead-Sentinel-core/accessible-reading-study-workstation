# Scope Statement — The Gates Lead Somewhere

> Written per the `scope-first` skill at onset, before any pseudocode or
> code. Status: **BASELINED 2026-11-28 by Falcon One**, as drafted, with
> no amendments. Changes after baseline are explicit logged decisions
> (one line in `Assistant-Notes.md` §5), never drift.
> Standards frame: ISO/IEC/IEEE 12207 · SWEBOK · IEEE 29148.

_Drafted: 2026-11-28 · Baselined: 2026-11-28 · Owner: Shannon Brian Kelley (Falcon One) ·
Foreman: Claude (Falcon Two). Parent baseline: `docs/SCOPE.md`._

## 0. The defect this answers

Reported by the owner 2026-11-28, in his words: *"it doesn't matter what
gate you click on, it always shows the first goal for the mental gate …
every time I try to add something to one of the gates, the gate's goal
shows up in a different goal."*

**Measured in the source at `d36b474`, not guessed:**

| # | Finding | Evidence |
| --- | --- | --- |
| 1 | The goals list is **never filtered by area** | `_refresh_list` runs `SELECT id,title,progress,status,target_date,created_at FROM goals ORDER BY (status='done'), id DESC` — no `life_area`, no `WHERE` |
| 2 | `life_area` is **write-only** | It appears in exactly three statements in 28,877 lines: the single-goal load, the INSERT, the UPDATE |
| 3 | Two **silent declines** on the gate path | `_area_goal` skips the prefill with no breadcrumb when the hook is missing; `_prefill_goal_area` swallows `tk.TclError` |
| 4 | The goals Listbox has **no `exportselection=False`** | CRUD listbox on Tk defaults — Law 6 item 1, a class already paid for twice |
| 5 | A second door bypasses the prefill | `🎯 Set goals on weak areas` is wired `command=goto_goals` — screen switch only, no clear, no area |
| 6 | The regression gate **does not run the code** | `test_wheel_buttons_wired_to_goals_prefill` is a string match over the AST for the name `_zz_prefill_goal_area` |

Finding 1 alone produces the reported symptom. Findings 3–5 explain why it
was unexplainable from the chair, and finding 4 is the half that silently
edits an existing goal instead of creating a new one.

**Law 1 could not be satisfied and that is recorded, not papered over.**
`qa_debug.log` on the live station is current (last write 2026-11-28
00:06), but `goal`, `area`, `gate` and `prefill` return **zero matches**
across its 43 KB. The Goals flow emits no breadcrumbs at all. The
diagnosis above is therefore source-measured, not log-confirmed, and one
question stays **open**: whether the area badge shows the correct gate
after a gate click. Acceptance A3 settles it.

**Station note — CORRECTED 2026-11-28, same day it was written.** The
drafted version of this paragraph announced the live install at
`C:\Users\sbrya\OneDrive\Sentinel personal development` as a *third
station nobody had counted*. That was wrong, and the shop's own paperwork
said so already: punch **#16** boarded exactly this on 2026-11-17, and
`docs/wiki/Development-Workflow.md` §1 has drawn **all four stations** —
live install, GitHub, laptop, old live install — since that walk. The
foreman wrote the claim before reading the punch list, which is the same
Law 1 error in a different coat. What is true and worth keeping: all four
stations read `d36b474` at drafting, so the code measured in §0 is the code
the owner is running.

## 1. In scope

1. **The gate filters the list.** The goals list shows the goals of the
   area whose gate you walked through, and says which area it is showing.
   An area with no goals yet gets an explicit empty state in words.
2. **Every door into Goals lands on a defined state.** A named gate lands
   on a blank worksheet with that gate's area on the badge and the cursor
   in the Goal line. The `🎯 Set goals on weak areas` door gets a defined
   landing too — it must not hand over a stale form carrying a previous
   goal's row id.
3. **The path speaks (Law 3).** Every decline on the gate → Goals path
   writes a breadcrumb naming the reason and puts a sentence on the status
   line. No silent `pass`, no swallowed `TclError`.
4. **The listbox stops sharing its selection (Law 6 item 1).**
   `exportselection=False` on the goals Listbox.
5. **A gate that can fail (Law 5).** A regression test that executes the
   filter and the landing-state logic and fails if either regresses. The
   existing string-match test is replaced, not kept alongside.

## 2. Out of scope

- **No database schema change.** `life_area` already exists, is indexed
  (`idx_goals_area`) and is populated. This defect is a missing `WHERE`,
  not a missing column.
- **No redesign.** No new screens, no new navigation, no colour changes,
  no change to the badge, the gates, or the city-wall art.
- **Punch #21 and #22 are not touched** (calendar date field discarded;
  City Gates unreachable below gate 3). Separate tickets, separate scope.
- **No app-wide instrumentation sweep.** Breadcrumbs are added to the gate
  → Goals path only. A sweep would need its own static gate per Law 5.
- **No change to goal save semantics** beyond what item 2 requires to stop
  an accidental UPDATE. Editing an existing goal on purpose keeps working.
- **No station/mirror work.** The third-station finding is logged above and
  boarded; repairing the topology is not this sprint.
- **No new dependency.** Nothing is added to `requirements.txt`.

## 3. Acceptance criteria

| | Criterion | How it is proven |
| --- | --- | --- |
| **A1** | With goals saved in at least two areas, each gate lists only its own area's goals | Owner clicks Mental and Physical gates on his real screen and reports what he sees (Law 6: headless probes lie) |
| **A2** | A gate click lands on a blank worksheet, that gate's badge, cursor in the Goal line | Owner's run + breadcrumb from A3 |
| **A3** | Saving after a gate click **creates** a goal; the row count rises by one and no existing goal changes | `SELECT count(*)` before/after, plus the saved row's `life_area` equals the gate clicked |
| **A4** | `qa_debug.log` gains one line per gate click naming the area and whether the prefill ran, and a line for every decline | `grep -i gate qa_debug.log` returns entries after the owner's run — it returns none today |
| **A5** | Clicking into the Goal title field does not change which goal the form is pointed at | Owner's run; `exportselection=False` present in the source |
| **A6** | An area with no goals shows a worded empty state, not an empty box | Owner's run on a fresh area |
| **A7** | The regression test fails when the `WHERE` clause is deleted | Delete it locally, run `python -m unittest discover -s tests`, see red, restore |

A1, A2, A5 and A6 are the owner's UAT and are reported as what he saw —
not as a green bar. A3, A4 and A7 are mechanical and are reported as the
numbers they are.

## 4. Lifecycle target

Inherited from `docs/SCOPE.md`, unchanged by this sprint: local-first,
single user, no cloud dependency; Python 3.13 + Tk + sqlite3, stdlib
first; **3–5 years, single maintainer plus AI assistant.** Every item
above is stdlib-only and adds no dependency, because a dependency with a
shorter life than the project is a liability this sprint will not take on.

## 5. Signature

- [x] **Falcon One** — baselined 2026-11-28, as drafted, no amendments.

Nothing in §1 is built until that box is ticked. Pseudocode comes next,
per `classroom-code` Stage 2, and is reviewed before any line of Python.
