# Shop Punch List — the running ledger

Standing document, ordered by the proprietor 2026-07-25. Construction
vocabulary on purpose: a **punch list** is the trade's running record of
every item still open on a job, walked at each visit until every line is
struck. This one adds the classroom's discipline on top: every defect is
**classified**, classes are **tallied**, and a class that keeps recurring
gets a **🔴 red plum** — a standing order to stop patching instances and
trace the class to its origin. (The practice is textbook: defect
classification per IEEE 1044 plus trend analysis; the Former-Bugs page
is the *history*, this page is the *watch list*.)

**Foreman's duties on this page:** read it at every session start; add a
tally mark whenever a fix lands; strike lines when the owner's UAT
confirms; escalate any class reaching 3 marks to 🔴 and open a
trace-to-origin investigation as its own ticket.

---

## A. Defect-class tally (the red-plum board)

| Class | What it looks like | Marks | Status |
|---|---|---|---|
| Invisible state | control works but shows nothing (checkbox, meter, status — and now ART: drawn ≠ visible) | 10 (2026-07-27: the invisible skyline, values 1.17:1) | 🔴 red plum — standing design law: every action shows visible proof |
| Precondition quietly false | "button does nothing" because selection/focus/window silently invalid | 4 (2026-07-25: stolen selection, hidden confirm, ghost tab, empty curselection decline) | 🔴 red plum — decline paths must LOG (breadcrumb) and TELL (status line), never just return |
| Cross-cutting affordance missed | app-wide feature (clipboard menu, mic enrollment) skips one widget | 3 (glossary dialog, commentary dialog, earlier mic boxes) | 🔴 red plum — hand-applied sweeps always miss one; every sweep now ends with a static gate |
| Clipped/unreachable controls | last-packed rows starved off short windows; modal grabs freezing the toolbar; **content with no scroll container at all** | **4** (glossary row, commentary row, read-view row, **2026-11-19: City Gates list — gates 4–7 unreachable, see #22**) | 🔴 **RED PLUM — escalated 2026-11-19 by the board's own rule.** *Note: this class was already carrying 3 marks while still flagged ⚠ watch; by the stated rule (3 = 🔴) it should have gone red at the third. Correcting that now rather than leaving the board inconsistent with its own law.* Recurrence after a law and a gate were already in place makes this a **process failure**, not a code failure: the bottom-first law is gated in tests, but the gate only catches *starved packing* — it never checked for **the absence of a scroll container**, which is how this one got through |
| Heuristic where a contract belongs | search/guess dispatch missing in the field | 2 (find-a-save-button ×2 widenings) | ⚠ watch — rule: a second miss converts the heuristic to a registration |
| Stale lifetime (memory outlives owner) | `_study_active_tab` outliving its window | 1 (+ legacy handlers surviving by lucky TclError) | ⚠ watch — Blueprint §11 documents; sweep candidate below |
| Paperwork drifted from reality | a record states a path, slug, count or claim the repo no longer matches — and the next worker follows the record | **4** (2026-11-17, all four found in one session: the live-install path in two wiki pages · the pre-rename repo slug in `Development-Workflow.md` §1 · `SDLC_STATUS.md` current-state claims of 8 then 34 tests, 953 functions, 23.6k LOC · the `Session-Notes-and-Handoff.md` at-a-glance block at v0.9 / 34 tests / HEAD `aea48c8`) | 🔴 **RED PLUM — class enacted and escalated 2026-11-17 by the board's own mechanical rule (3 marks = 🔴), not by foreman fiat.** Trace-to-origin already visible: current-state facts are written in prose in many places with no single source of truth and no gate, so each page rots independently and the next worker trusts whichever one he opens. Named design law: **a document that states a current fact must be checkable, or it states history and says so.** Static gate owed: a headless test asserting (a) the live-install path and repo slug named in the wiki resolve to this checkout and this remote, and (b) any test count quoted in docs matches the suite's real size. Gate is NOT yet written — it is the one piece of code this close-out leaves owed |

**Rule:** 3 marks = 🔴. A 🔴 class gets a named design law, a static gate
where possible, and its next occurrence is treated as a process failure,
not a code failure — the question becomes "why did the law not hold?"

## B. Open punch items (walk at every session)

**Eisenhower triage 2026-07-25** (working order in
`docs/foreman/TOPICS.md`): DO → #3 (executed). SCHEDULE → cycles: #5,
then #4, then #9-implementation (blocked on delegate), then v1.0 cut
(proprietor's word). DELEGATE → #8, #9-scope-call (Falcon One).
DEFER → #6, #7 (scope-first before any code).

**Eisenhower triage 2026-07-30** (proprietor's order: DO-now queue
cleared, promote the deferred/scheduled items in order of date and
importance): **DO, foreman** → 'reader' ghost-tab defect (green-lit,
executed same session), then #5 silent-declines sweep (oldest open
engineering item, red-plum law, first motion next session). **DO,
Falcon One** → #11 signs UAT + 'reader'-fix UAT; Recycle Bin click
(C: at ~4 GB free); then #10 SUS scorecard (oldest open owner item,
2026-07-26). **SCHEDULE** → #4 legacy-handler sweep (rides behind #5,
same seam family); `.aitk` 20 GB relocation to E: (awaits owner OK);
hub-window signage extension (scope call). **DELEGATE** → Q3
warehouse freight to E: after the owner's pruning pass (foreman);
Imprint archive-ledger paperwork (concept, scoped when called).
**DEFER** → #6 Vault Catalog, #7 script-export, imaging node,
CleanroomIntake benchmark (owner's want, optional). **DELETE** →
nothing; the archive law stands.


**Eisenhower triage 2026-08-03 (proprietor's clear-the-board order:
everything green-lighted, nothing parked, Pomodoro execution):**
**DO NOW, foreman, one cycle each** → C1 ✅ warranty pair executed this
session (A−/A+ ceiling now SPEAKS “at MAXIMUM”; Treasury hub gained
wheel-scroll + wide slider so the 🔍 Zero-Based Audit door is reachable
— root cause: below-the-fold + no wheel binding; PLUS third live-DB
test-isolation leak fixed with temp_study_db in RetrieveContextRecursionTest).
C2 → hub-window signage. C3 → CleanroomIntake retrieval benchmark.
C4–C7 → scope statements, one per cycle, in order: #13 analytics panel,
#12 Prompt Fragment Vault, #6 Vault Catalog, #7 script-export; each
build follows its approved scope as its own sprint. **DELEGATE, Falcon
One** → five resume blanks · Carlton ask · #10 SUS · #4 spot-check ·
UAT tonight's two fixes (wheel reaches Audit; A+ names its MAXIMUM).
**SCHEDULE** → the C4–C7 builds behind their scopes. **DO LATER (real
constraints, not deferral)** → imaging node + portable container (await
hardware/funding per the owner's own condition). **DELETE** → nothing.

**COMPLETION DECLARATION 2026-07-30 (proprietor's word, on the
record):** Sentinel Forge — Personal Development is **DONE**. The
house is built, inspected, and occupied (final walk-through
certificate: Claude AI\Portfoliooards6-07-30_FinalWalkthrough
.md — FIT FOR OCCUPANCY). The promote-the-deferred queue is
re-parked as OPTIONAL post-completion backlog — built only if the
proprietor ever orders it, owed to no one. The shop stands in
MAINTENANCE MODE: defects found in daily use get fixed under warranty;
nothing new gets built without a fresh scope. SUS scorecard remains a
measurement of the finished product, not a build item.

| # | Item | Origin | State |
|---|---|---|---|
| 1 | Owner UAT: full CRUD cycle on Topics after 68fb199 (delete topic+7 entries, add fresh, delete again) | 2026-07-25 ticket 4 | ~~STRUCK~~ — owner UAT ✅ 2026-07-25 ("read, saved, deleted, copied and pasted into every section") |
| 2 | Owner UAT: paste → ➕ Add lands entries in all three sections (b73a7cf flow) | 2026-07-25 ticket 3 | ~~STRUCK~~ — owner UAT ✅ 2026-07-25; Matrix + all three planners also UAT-passed with toolbar add/remove/mark-off |
| 3 | Read-only glossary view has no copy-out clipboard menu | 2026-07-25 audit | ~~STRUCK~~ — Eisenhower DO, executed 2026-07-25 (Copy + Select-all menu; gated) |
| 4 | Legacy save/remove handlers survive ghost-tab only via lucky TclError — sweep to explicit window checks | Blueprint §11 trap | EXECUTED 2026-07-30 — finding: NO TclError luck existed (window withdraws, widgets live); `_study_workspace_visible()` one-seam guard on all 5 tab claims + add route; 3 gates. Gates + smoke green; owner startup UAT ✅ (no error flash, clean landing). Optional 10-second spot-check remains open: workspace CLOSED → yellow Save from dashboard → expect the honest “nothing to save” line |
| 5 | Decline paths in `_ftb_action_*` chains: several return silently with neither breadcrumb nor status | red-plum class 2 | ~~STRUCK~~ — owner UAT ✅ 2026-07-30: empty journal + Save → spoken refusal on screen; notes save + spoken empty-decline verified; no silent dead-air anywhere on his walk |
| 6 | Vault Catalog (optical/external media index): archive-set export + media catalog table in study.db | owner's 2026-07-25 optical-media intake | BACKLOG — scope-first + blueprint before any code |
| 7 | Script-export pipeline for narrated educational segments (notes/glossary → script text for outside video tools) | same intake | BACKLOG — idea only, no scope yet |
| 8 | E: drive verification (E: = the 1TB external backup HDD); ~~7 unmerged branches~~ | journal 2026-07-20 | ~~STRUCK~~ — branch verdict ✅ 2026-07-26 (GitHub = main only). E: half ✅ 2026-07-30: drive mounted, NTFS healthy (931.5 GB / 718.7 free), write/read proven; Q1 storm-shelter clone landed (study.db 220 MB zero-fail, 3 repo bundles); .aitk 19.75 GB relocated via junction (zero-fail copy); folder clone pass 2 in flight |
| 10 | SUS baseline (Law 7, A-grade doctrine): proprietor takes the 10-question scorecard cold against v1.0+F-series (`docs/foreman/SUS-SCORECARD.md`), re-measures after ~2-3 weeks of daily use; target ≥85, shortfalls reported as-is | proprietor's order 2026-07-26 | OPEN — awaiting first administration |
| 9 | AI assistant grounding gaps | owner status report 2026-07-25 | ~~STRUCK~~ — scope call ✅ 2026-07-26 (proprietor: ALL FOUR sections) and implemented same session: commentaries, topic-entry bodies, Matrix, Planner added to the grounding feed (lyceum/local_context.py); headless test seeds one row per section and proves retrieval |
| 11 | Room signs: universal pictogram + word signage per panel/window (AAC picture-board principle, ISO 7001 pictograms, recognition-over-recall; extends the shipped traffic-light design language; one shared header seam) | owner's 2026-07-29 intake; board `Claude AI\Portfolio\boards\2026-07-29_RoomSigns.md` | SHIPPED (owner green light same night) — kernel `lyceum/room_signs.py` + `_draw_room_sign` seam in the study-tab loop; all 8 study rooms signed; 14 tests + static gate; smoke 8/8; suite 520 green. ~~STRUCK~~ — owner UAT ✅ 2026-07-30 ("did the walk, all eight tabs, all okay"). Hub windows (Library, Money Hub, …) NOT yet signed — extension queued in the authorized promote-the-deferred order |

| 12 | Prompt Fragment Vault: procedural-knowledge harvest from the Prompt Library (declarative→Glossary/FSRS stays as-is; procedural fragments→new additive vault table→Prompt Coach snippets). Payload admitted from a Gemini-costumed proposal per the costume-vs-payload precedent (2026-07-27); costume rejected; re-derive pseudocode before any build | owner's 2026-07-31 study session (his observation, his credit) | BACKLOG — scope-first + blueprint; shop in maintenance mode; Do Now is the job campaign |

| 13 | Progress Observatory: ONE descriptive-analytics panel answering the stakeholder question “effort, attempts, misses, supports used, consistency over time” from existing local records (aggregation only; no prediction — n-of-one overfits; admission rule ratified 2026-08-03) | owner's data-analytics coursework session | GREEN-LIT — scope-first doc = cycle C4 |

| 14 | Store-release hardening scope (`docs/SCOPE_STORE_RELEASE.md`): build repair, portability pass, privacy policy, MSIX, WACK certification, IP-clean pass (Pomodoro → "Focus Cycles"), Partner Center listing at $29.95 one-time. Carries acceptance criteria A1–A6 | foreman's 2026-08-06 sprint draft — **found unboarded on branch `forge-work` during the 2026-11-17 walk** | OPEN — **PROPOSED, awaiting Falcon One sign-off** since 2026-08-06. Three commits (`de0f49c`, `00d78fd`, `3bdfa34`) unmerged, 3 ahead / 4 behind `main`. **Pre-signature audit filed 2026-11-17** (`docs/foreman/STORE_SCOPE_PRESIGN_AUDIT_2026-11-17.md`, doc_id `SPD-FOREMAN-STOREAUDIT-001`): every claim measured against the code. Trademark exposure is **one** UI string (line 27877), not a sweep — the rest is comments, identifiers and DB schema names that `SCOPE.md`'s additive-only law says to leave alone. A3 already half-shipped by `lyceum/db/db_location.py`. Portability debt is one seam (`_onedrive_root()`) + three literals (lines 107/108/118). **None of pyinstaller / makeappx / signtool / WACK is installed** — unaccounted for in the scope. Four amendments A–D proposed; foreman recommends signing with them folded in. Triage N1 |
| 15 | Mirror-law breach, two stations: laptop `C:\Users\sbrya\Desktop\Sentinel personal Development` was `main` @ `056a6f7`, clean but **109 commits behind** (files 2026-07-16, pre-v1.0); worktree `C:\Users\sbrya\OneDrive\Desktop\Sentinel-Forge` was `main` @ `1177f65` with `sentinel_personal_development.py` + `sentinel.ico` **deleted** — that copy could not launch the app | 2026-11-17 board-clearing walk | ~~STRUCK~~ — owner ordered "push and sync" 2026-11-17; executed and verified. `7e8a200` pushed to GitHub (`1fc3c68..7e8a200`), both stations fast-forwarded, the two deleted files restored. **All four stations now report `7e8a200`, zero changed paths, and `sentinel_personal_development.py` byte-identical at SHA-256 `6473B149237DFFAC…` on every one** — SCOPE.md §3 satisfied by measurement, not assertion. Before destroying the one uncommitted change (`docs/PORTFOLIO_AUDIT.md` at the fourth station) its blob was compared against `origin/main`: **identical**, so nothing was lost — his own golden rule, *compare before you destroy* |
| 16 | Paperwork names the wrong live install: `Session-Notes-and-Handoff.md` and `Development-Workflow.md` both instruct editing `Desktop\Sentinel-Forge`, but the shortcut, the last run, and HEAD all say the live install is `OneDrive\Sentinel personal development`. The workflow page also still carried the pre-rename repo slug and the claim that laptop and OneDrive "are the SAME files" | 2026-11-17 board-clearing walk | ~~STRUCK~~ — foreman evidence, committed in `7e8a200`: §1 rewritten as **four stations**, the real live-install path named, the post-rename slug (`accessible-reading-study-workstation`) corrected, and the Desktop-is-not-OneDrive-Desktop trap written down in the words that caused it. History sections left as written — the archive law applies to the record, not to the instructions |
| 19 | Suite count documented but not demonstrated: README claimed 536 tests since `e764e80` (2026-08-23), never re-run | triage N8, 2026-11-17 | ~~STRUCK~~ — **run 2026-11-17: `Ran 536 tests in 97.807s` · `OK (skipped=14)`** across 53 modules. The README was exact. Stale *current-state* claims it exposed elsewhere were corrected in the same pass: `SDLC_STATUS.md` (said 8 and 34 tests, 953 functions, 23.6k LOC → now 536 tests, 1,104 functions, 28,537 lines, `BookReader` 667 methods, and the professor's 2026-06-27 verdict marked answered) and the `Session-Notes-and-Handoff.md` at-a-glance block (said v0.9 / 34 tests / HEAD `aea48c8` → now v1.0.0, 536, four synced stations; old snapshot folded away as history, not deleted) |
| 17 | OneDrive placeholder-hydration risk: files in the live install carried `RECALL_ON_DATA_ACCESS`. They hydrate on demand but a suite run, a PyInstaller build, or an offline start touches all of them at once — the exact failure that stopped the EARP suite with 25 such files | 2026-11-17 board-clearing walk | ~~STRUCK~~ — owner green-lit 2026-11-17; executed and measured. Full-tree count was **930 files, 127 unhydrated** (the earlier "180 of 198" counted only the tracked subset — corrected here rather than left standing). `attrib +p /s /d` applied: **930 of 930 now PINNED, 0 stubs.** Pinning only *queues* OneDrive's download, so hydration was then forced file-by-file rather than left to the daemon; **4 files failed on the first pass and succeeded on retry** (`CHANGELOG.md`, `tests/gui_base.py`, `tests/test_automation.py`, `tests/test_voice_pipeline.py`) — the same retry lesson the EARP shelter clone paid for. 25.5 MB on disk, C: at 33.8 GB free |
| 20 | Orphaned git worktree holding `forge-work`: a stale Claude Code worktree at `OneDrive\Desktop\.claude\worktrees\sentinel-personal-development` had the branch checked out at `3bdfa34`, which is why the branch could not be deleted. A **fifth** copy of the project nobody had counted | surfaced 2026-11-17 while executing the owner's branch-deletion order | ~~STRUCK~~ — verified redundant before anything was removed: clean tree, **0 commits not in `main`**, every file a duplicate of main's history. Branch `forge-work` deleted (was `3bdfa34`, recorded for reversal; all three of its commits — `de0f49c`, `00d78fd`, `3bdfa34` — confirmed reachable from `main`). `git worktree remove` was refused by 23 read-only files; attributes cleared on that path only, directory removed, stale `.git/worktrees/` metadata cleared, `git worktree prune` run. **One registered worktree remains, which is `main` itself.** Three other worktrees live under that folder (`imprint`, `strata`, `ecstatic-feynman-be61f1`) — other projects, deliberately untouched |
| 18 | Field observation, review Delete: 18 `ftb-review: DELETE claimed` breadcrumbs on 2026-11-17 01:13–02:48 — 2 cleared on today, 16 refused across nine past dates, five of those days re-pressed inside 1.3 s. Code inspected: `_review_remove_from_toolbar` breadcrumbs **and** speaks its refusal, so punch #5's law is honored in the letter. Open question is whether the status line registered | 2026-11-17 board-clearing walk, from his own run | OPEN — **not yet a defect.** One owner answer decides: working-as-designed, or a 🔴 invisible-state recurrence (class at 10 marks). Triage N3 |
| 23 | Goals room ignored the gate you walked through: the list query had **no `WHERE` clause** and `life_area` was **write-only** (3 statements in 28,877 lines), so every gate showed the same unfiltered list headed by the highest id — reported as *"it always shows the first goal for the mental gate"*. Second half: the purple weak-areas button was wired straight to the screen switch, handing over a stale form **still carrying the loaded goal's row id**, so the next Save was an UPDATE of an old goal — *"the gate's goal shows up in a different goal"* | owner report 2026-11-28, from his own run | **FIXED IN THE TREE, UNCOMMITTED, OWNER UAT OUTSTANDING.** Scope `docs/SCOPE_GOALS_AREA_FILTER.md` (baselined 2026-11-28), blueprint `docs/BLUEPRINT_GOALS_AREA_FILTER.md`. Filter is pure and unit-tested (`lyceum.goals.list_query`); both doors now enter through one `EnterGoalsRoom` contract; `exportselection=False` added (Law 6 item 1); the whole path breadcrumbs (it emitted **zero** before — grep of the live 43 KB `qa_debug.log` for `goal`/`area`/`gate`/`prefill` returned nothing, so **Law 1 could not be satisfied** and the diagnosis is source-measured, not log-confirmed). The old gate `test_wheel_buttons_wired_to_goals_prefill` was a **string match that never ran a line** and stayed green throughout — removed, replaced by two suites that execute the behaviour. **A7 demonstrated:** deleting the `WHERE` turns the suite red. Suite **593** green, `OK (skipped=14)`. Acceptance **A1, A2, A5, A6 are the owner's run on the real screen** — Law 6: headless probes have passed here while real clicks failed |
| 24 | Laptop station still points at the **pre-rename** remote: `C:\Users\sbrya\Desktop\Sentinel personal Development` has `origin` = `sentinel-forge-personal-development`, while the live install and `Desktop\Sentinel-Forge` both carry the current `accessible-reading-study-workstation`. It fetches and pushes correctly **only because GitHub redirects a renamed repository** — a redirect the owner can remove at any time, and one that hides which repo a station is really talking to | measured 2026-11-28 while filing #23 | OPEN — one `git remote set-url` on that station fixes it; the owner's word, not the foreman's, since it touches a station. *Note: while checking this the foreman first suspected the slug in `Development-Workflow.md` §1 was stale. It is not — the doc is correct and the laptop is the odd one out. Recorded so the wrong suspicion does not get re-derived later* |

**EISENHOWER WALK 2026-11-17 (proprietor's order: "make sure that
everything on the board is cleared"):** every open line above now carries a
bucket in his own four — DUE NOW, DUE LATER, DEFERRED, SCHEDULED. Triage of
record, with Nexus node routing, the pseudocode call, and the three-point
mirror table: `docs/foreman/EISENHOWER_A1_2026-11-17.md` (doc_id
`SPD-FOREMAN-EISENHOWER-001`); working order mirrored into
`docs/foreman/TOPICS.md`. Lines 14–18 were added by that walk — four of the
five were invisible to this page before it. No tally marks added: no fix
landed this session, and a walk is not a fix.

| 21 | Goals worksheet: "📅 Add next step to calendar on:" accepts a date, but the planner entry lands on **today** regardless. Owner confirmed in the field twice (2026-11-18 set to 11-20 → landed 11-18; 2026-11-19 set to 11-20 → landed 11-19) | owner's daily use, 2026-11-19 | OPEN — **ROOT CAUSE LOCATED, not yet fixed.** The `_add_to_calendar` handler at `sentinel_personal_development.py:25058` is **innocent** — it reads `day_e.get()` into `dstr`, validates the format, and inserts with `dstr`. The defect is the **flow-carry path at ~:25259**, which hardcodes `today = date.today().strftime("%Y-%m-%d")` and INSERTs the goal's next step into `planner_tasks` on **today**, ignoring the date entry entirely. It fires on save / check-in — the same carry-the-data-forward mechanism that pushes the goal into the Matrix Do Now. **Candidate fix:** pass the chosen date down from the goals panel into the flow-carry call instead of letting it default to `date.today()`; fall back to today only when the field is empty. **Gate owed:** a headless test that sets the date field to a non-today value, saves, and asserts the planner row's `day` matches. Owner will take it on his next day off |

**Defect-class note for #21.** This is NOT "a control that does nothing" — it is worse: **a control that accepts the user's input and silently substitutes its own value.** The status line even reports the correct date (`Added to {dstr}`) while a second writer puts the row somewhere else, so the app tells the truth and still produces the wrong result. For an owner who uses the planner as external memory, a task filed on the wrong day is a task missed. Recommend this seeds a new tally: **"input accepted, then discarded"** — 1 mark, pending the proprietor's ratification.

| 22 | City Gates list is cut off — only gates 1–3 (Mental, Spiritual, Physical) reachable. Family, Financial, Career and Social fall below the fold with no way to scroll to them. Blocks the walk after the first gate | owner's daily use, 2026-11-19 | OPEN — **ROOT CAUSE CONFIRMED IN SOURCE, and it is not the amount of text.** `sentinel_personal_development.py:13286`: `ss_frames[key] = tk.Frame(content, bg=BG_DARK)` — the Session Start panels are **plain Frames with no Canvas + Scrollbar**, so anything taller than the window is simply unreachable. On a ~1097×617 display the header art plus the gate rows exhaust the height by gate three. **The fix already exists in this codebase:** the dashboard at `:646–672` uses exactly the right scaffold — `dash_canvas` + `dash_vsb` + `yscrollcommand` + a `<Configure>` handler setting `scrollregion=bbox("all")`. Wrap the Session Start panels in that same pattern. **Gate owed:** extend the bottom-first test so it asserts every scrollable panel HAS a scroll container, not merely that the last row packed |

**Workarounds available today, before the fix lands (#22).** 1) Press **A−** in the toolbar to shrink the font — more rows fit the same height. 2) Maximize or **Undock** the window. 3) **Route around the gate buttons entirely:** the purple **🎯 Set goals on weak areas** button opens the Goals panel directly, where **Life area** can be set by hand. The walk can continue on any gate using this route. *Updated 2026-11-28 (#23): that button now enters by the same contract as the gates — it clears the worksheet and shows **every area**, where a named gate shows only its own. So the route still works, but it is no longer equivalent to walking through the gate: set **Life area** by hand and expect the unfiltered list.*

## C. How a line moves

OPEN → owner UAT / foreman evidence → STRUCK (moved to Former-Bugs or
CHANGELOG with its lesson) — or → BACKLOG (wanted, not scoped) — or
→ 🔴 investigation (recurrence traced to origin; outcome is a design
law + gate). Nothing is deleted from this page; struck lines move to
the history pages. The ledger is the memory; the red plums are the
alarm.
