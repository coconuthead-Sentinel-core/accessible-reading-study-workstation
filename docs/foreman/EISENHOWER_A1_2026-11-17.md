# Eisenhower Triage — A1 Filing System

```yaml
doc_id: SPD-FOREMAN-EISENHOWER-001
title: Eisenhower Triage of the Shop Punch List — board-clearing walk 2026-11-17
zone: GREEN
cognitive_load: 8
timestamp: 2026-11-17T00:00:00Z
status: ACTIVE
author: Shannon Brian Kelley (Falcon One) / Claude, shop foreman (Falcon Two)
version: v001
naming: SPD-FOREMAN-eisenhower_2026-11-17_v001
parent_ledger: docs/wiki/Shop-Punch-List.md
working_order: docs/foreman/TOPICS.md
```

Ordered by Falcon One, 2026-11-17: *"use the Eisenhower matrix in the A1
filing system … make sure everything on the board is cleared."* Buckets are
the proprietor's own four, in the order he named them. The punch list stays
the **ledger of record**; this page is the **triage of record** for this walk.

**Bucket → classic quadrant.** DUE NOW = urgent + important (Q1, do).
DUE LATER = important, not urgent, held by a real external constraint
(Q2 held by reality, not by choice). DEFERRED = important, not urgent, not
started by decision (Q2 parked behind a scope gate). SCHEDULED = queued with
a named trigger (Q2 with a date or a dependency).

**Nexus node routing.** The lattice (`Forge-Stack-A1/01_BACK_END/
node_registry.md`) is the SPN orchestration layer, not a wired dependency of
this Tk app — so the node column below is an **honest work-type routing**
drawn from the A1 query interface (RETRIEVAL→NODE-002, BUILD→NODE-005,
SYNC→NODE-004, HANDOFF→NODE-003, ROUTE→NODE-007), with the QNF layer naming
who decides. Labels, not couplings; said plainly so nobody later mistakes a
label for an integration.

---

## 1. DUE NOW — this cycle

| ID | Item | Owner | Node | Why now |
|---|---|---|---|---|
| N1 | **Store-release scope sign-off.** `docs/SCOPE_STORE_RELEASE.md` is PROPOSED and has sat unmerged on branch `forge-work` since 2026-08-06, never boarded on the punch list. Carries the $29.95 one-time price decision and the IP audit. | Falcon One | NODE-010 SHANNON-PRIME | Oldest *decision* on the board, and the only thread with revenue on it. Nothing in the Store sprint can start without his signature. |
| N2 | **Punch #10 SUS baseline.** Cold 10-question administration, `docs/foreman/SUS-SCORECARD.md`, target ≥ 85, shortfalls reported as-is. | Falcon One | NODE-015 MIRROR | Open since 2026-07-26 — oldest open line of any kind. Law 7 requires the measured bar, and three months of daily field time is exactly the condition it was waiting for. |
| N3 | **Field question — the review Delete.** 2026-11-17 01:13–02:48, `qa_debug.log` records 18 `ftb-review: DELETE claimed` events: 2 cleared on today, 16 refused across nine past dates (10-17, 07-20 ×3, 07-15 ×2, 07-07 ×2, 06-28 ×2, 06-27 ×2, 06-21, 06-20, 06-16, 06-11). Five of those days were re-pressed inside 1.3 s. | Falcon One | NODE-014 CHALLENGE | The code is innocent on inspection — `_review_remove_from_toolbar` both breadcrumbs AND speaks ("Past reviews are history — never deleted"). So the open question is whether he SAW that line. One answer decides between "working as designed" and a 🔴 invisible-state recurrence. |
| N4 | **Laptop station is 109 commits behind.** `C:\Users\sbrya\Desktop\Sentinel personal Development` — `main` @ `056a6f7`, tree clean, files dated 2026-07-16. Verified a fast-forward ancestor of `1fc3c68`, so a pull is safe and `git reset --hard 056a6f7` reverses it. | Foreman, on his word | NODE-004 GitHub-Sync | SCOPE.md §3 makes mirror agreement an acceptance criterion. One station is four months and an entire v1.0 release out of compliance. |
| N5 | **Fourth station is damaged.** `C:\Users\sbrya\OneDrive\Desktop\Sentinel-Forge` — `main` @ `1177f65` (4 behind) with `sentinel_personal_development.py` and `sentinel.ico` showing as **deleted**. That copy cannot launch the app. Repair-or-retire is a proprietor call. | Falcon One decides, foreman executes | NODE-004 GitHub-Sync | A station that cannot run the product is not a mirror. Either it comes back to `1fc3c68` or it is formally struck from the mirror law. |
| N6 | **Paperwork names the wrong live install.** `docs/wiki/Session-Notes-and-Handoff.md` and `Development-Workflow.md` still say to edit `Desktop\Sentinel-Forge`. The shortcut, the last run, and HEAD all say the live install is `OneDrive\Sentinel personal development`. | Foreman | NODE-003 Handoff-Manager | Same defect class as the EARP `src/` find: the code moved and the paperwork didn't. Wrong instructions are worse than no instructions. |
| N7 | **180 of 198 files in the live install are unhydrated OneDrive placeholders.** They do hydrate on demand (`ai_brain.py` proved it this session), but a suite run, a PyInstaller build, or an offline start touches all of them at once. | Falcon One (his disk) | NODE-006 File-Indexer | This is the exact EARP failure mode — 25 pointer files stopped that suite dead. Fix is one pin: `attrib +p /s` over the folder, or Explorer → *Always keep on this device*. The repo is small; the download is megabytes, not gigabytes. |
| N8 | **Suite count unverified.** README claims **536 tests** (commit `e764e80`, 2026-08-23). Not re-run this session — no code was touched, so nothing was owed, but it is the gate ahead of any fix. | Foreman, next cycle | NODE-005 Context-Packager | Honest-reporting law: the number in the README is documented, not demonstrated. It gets demonstrated before any code lands. |

## 2. DUE LATER — held by a real constraint, not by choice

| ID | Item | Constraint |
|---|---|---|
| L1 | Imaging node + portable container | Awaits hardware and funding — the proprietor's own stated condition, carried from the 2026-08-03 triage. Not deferral; arithmetic. |
| L2 | E: storm-shelter re-verification (study.db, repo bundles, the 19.75 GB model store, MANIFEST) | **E: was not mounted at this walk.** Verifiable only with the 1 TB external plugged in. A trigger, not a date. |
| L3 | Imprint-style archive-ledger paperwork | Concept accepted 2026-07-30; scoped when called. |

## 3. DEFERRED — wanted, parked behind the scope-first gate

| ID | Punch | Item | Gate |
|---|---|---|---|
| D1 | #12 | Prompt Fragment Vault — procedural-knowledge harvest from the Prompt Library into an additive vault table | Scope statement + **pseudocode re-derived** (the board already requires it by name — the Gemini-costumed proposal's payload was admitted, its costume rejected) |
| D2 | #6 | Vault Catalog — archive-set export + optical/external media index in `study.db` | Scope-first + blueprint |
| D3 | #7 | Script-export pipeline — notes/glossary → narration script text for outside video tools | Idea only; no scope exists |
| D4 | C3 | CleanroomIntake retrieval benchmark | The proprietor's want, explicitly optional |

## 4. SCHEDULED — queued, each with a named trigger

| ID | Item | Trigger | Node |
|---|---|---|---|
| S1 | Merge `forge-work` → `main` (3 docs commits: the Store scope, the price decision, the IP audit) | N1 sign-off | NODE-004 |
| S2 | **Pomodoro → "Focus Cycles" rename + a static gate keeping the mark out of shipped UI strings.** Registered trademark (Cirillo), actively enforced against timer software. | First item of the Store sprint, on N1 sign-off | NODE-005 |
| S3 | `Sentinel-Forge.spec` build repair — the spec names an entry point the repo does not have | Store sprint, behind S2 | NODE-005 |
| S4 | Punch #13 Progress Observatory — **scope statement** (cycle C4, green-lit 2026-08-03, never written). Descriptive aggregation only; no prediction (n-of-one overfits — admission rule ratified) | Next build cycle the proprietor opens | NODE-005 |
| S5 | Punch #11 / C2 hub-window signage — extend `lyceum/room_signs.py` to Library, Money Hub and the other hub windows. Study rooms shipped and struck; hubs never signed. | Scope call from Falcon One | NODE-005 |
| S6 | Punch #4 residual — the 10-second spot-check: workspace CLOSED → yellow Save from the dashboard → expect the honest "nothing to save" line | Next time he is at the dashboard | NODE-015 |

---

## 5. Board-clearing attestation

Every open line carried on `Shop-Punch-List.md` §B at this walk — #4
residual, #6, #7, #10, #11, #12, #13, C2, C3, the imaging node, the Imprint
paperwork — now holds a bucket above. Three threads were **added by this
walk** and boarded for the first time: the parked Store-release scope (N1,
S1–S3), the station/mirror findings (N4, N5, N6), and the placeholder
hydration risk (N7). Nothing is unassigned. Nothing was deleted — the
archive law stands.

**Red-plum board unchanged this walk** (no fixes landed, so no tally marks
were added): Invisible state 10 🔴 · Precondition quietly false 4 🔴 ·
Cross-cutting affordance missed 3 🔴 · Clipped/unreachable 3 ⚠ · Heuristic
where a contract belongs 2 ⚠ · Stale lifetime 1 ⚠.

## 6. Pseudocode call — nothing owed this session

`classroom-code` puts pseudocode before code; `scope-first` puts scope before
pseudocode. Walking the board against that order: no item in DUE NOW is a
code change (N1–N3 are decisions and a UAT answer; N4–N7 are sync, paperwork
and a storage setting; N8 is a test run). Every item that *will* need
pseudocode — S2, S3, S4, S5, D1 — sits behind an unwritten or unsigned scope
statement. Writing pseudocode now would be building on paper that has not
been baselined, which is the drift the rule book exists to stop.

**Verdict: no pseudocode is owed. The next artifact owed is a scope
statement — N1's signature, then S4's scope doc.** The first pseudocode of
the next build cycle goes on the board via `pseudocode-display`, as always.

## 7. Three points of reference — mirror state at this walk

| Station | Path / remote | HEAD | State |
|---|---|---|---|
| **GitHub** | `coconuthead-Sentinel-core/accessible-reading-study-workstation` | `1fc3c68` | ✅ fetched this walk; `main` agrees exactly, 0 ahead / 0 behind |
| **OneDrive** (= the live install) | `C:\Users\sbrya\OneDrive\Sentinel personal development` | `1fc3c68` | ✅ clean tree, in sync with GitHub. Launched by the desktop shortcut; ran last night 01:13–02:48 |
| **Laptop** | `C:\Users\sbrya\Desktop\Sentinel personal Development` | `056a6f7` | ❌ clean but **109 commits behind** (files dated 2026-07-16, pre-v1.0) |
| **Worktree / old live install** | `C:\Users\sbrya\OneDrive\Desktop\Sentinel-Forge` | `1177f65` | ❌ 4 behind **and** entry point + icon deleted; `M docs/PORTFOLIO_AUDIT.md` |

Tags present: `v0.9-rc1`, `v1.0.0`. Branches: `main`, `forge-work` (3 ahead
/ 4 behind). **Nothing was owed to GitHub before this session** — the live
repo was clean at the fetched remote hash. What this session created is
paperwork, and that is what the commit carries.

— *Claude, shop foreman & Archivist of Wisdom, Sentinel's Forge*
