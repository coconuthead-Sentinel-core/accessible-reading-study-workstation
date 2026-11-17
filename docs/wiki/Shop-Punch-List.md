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
| Clipped/unreachable controls | last-packed rows starved off short windows; modal grabs freezing the toolbar | 3 (glossary row, commentary row, read-view row) | ⚠ watch — bottom-first law gated in tests |
| Heuristic where a contract belongs | search/guess dispatch missing in the field | 2 (find-a-save-button ×2 widenings) | ⚠ watch — rule: a second miss converts the heuristic to a registration |
| Stale lifetime (memory outlives owner) | `_study_active_tab` outliving its window | 1 (+ legacy handlers surviving by lucky TclError) | ⚠ watch — Blueprint §11 documents; sweep candidate below |
| Paperwork drifted from reality | a record states a path, slug, count or claim the repo no longer matches — and the next worker follows the record | 2 (2026-11-17: the live-install path in two wiki pages; the pre-rename repo slug in `Development-Workflow.md` §1) | ⚠ watch — **PROPOSED class, awaiting Falcon One's ratification; the foreman does not enact shop law.** The breach it caused is punch #15: a station drifted 109 commits because a document said two different folders were the same files. Candidate gate: a headless test asserting that the live-install path and repo slug named in the wiki resolve to this checkout and this remote |

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
| 17 | OneDrive placeholder-hydration risk: **180 of 198 files** in the live install carry `RECALL_ON_DATA_ACCESS`. They hydrate on demand (proven on `ai_brain.py` this session) but a suite run, a PyInstaller build, or an offline start touches all of them at once — the exact failure that stopped the EARP suite with 25 such files | 2026-11-17 board-clearing walk | OPEN — one fix: `attrib +p /s` over the folder, or Explorer → *Always keep on this device*. Owner's disk, owner's click. Triage N7 |
| 18 | Field observation, review Delete: 18 `ftb-review: DELETE claimed` breadcrumbs on 2026-11-17 01:13–02:48 — 2 cleared on today, 16 refused across nine past dates, five of those days re-pressed inside 1.3 s. Code inspected: `_review_remove_from_toolbar` breadcrumbs **and** speaks its refusal, so punch #5's law is honored in the letter. Open question is whether the status line registered | 2026-11-17 board-clearing walk, from his own run | OPEN — **not yet a defect.** One owner answer decides: working-as-designed, or a 🔴 invisible-state recurrence (class at 10 marks). Triage N3 |

**EISENHOWER WALK 2026-11-17 (proprietor's order: "make sure that
everything on the board is cleared"):** every open line above now carries a
bucket in his own four — DUE NOW, DUE LATER, DEFERRED, SCHEDULED. Triage of
record, with Nexus node routing, the pseudocode call, and the three-point
mirror table: `docs/foreman/EISENHOWER_A1_2026-11-17.md` (doc_id
`SPD-FOREMAN-EISENHOWER-001`); working order mirrored into
`docs/foreman/TOPICS.md`. Lines 14–18 were added by that walk — four of the
five were invisible to this page before it. No tally marks added: no fix
landed this session, and a walk is not a fix.

## C. How a line moves

OPEN → owner UAT / foreman evidence → STRUCK (moved to Former-Bugs or
CHANGELOG with its lesson) — or → BACKLOG (wanted, not scoped) — or
→ 🔴 investigation (recurrence traced to origin; outcome is a design
law + gate). Nothing is deleted from this page; struck lines move to
the history pages. The ledger is the memory; the red plums are the
alarm.
