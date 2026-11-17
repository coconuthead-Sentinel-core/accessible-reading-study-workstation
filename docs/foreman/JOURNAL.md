# 📓 Foreman's Journal — work-cycle entries

(The shop-floor narrative journal remains
`Claude AI\SENTINELS_FORGE_FOREMANS_JOURNAL.md`; this file is the
foreman's WORKING journal — terse, cycle-by-cycle, in the repo so it
mirrors with the code it describes.)

## 2026-07-25 — Triage entry

- Proprietor's UAT report accepted: core workflows validated (Library
  CRUD, paste into all sections, Matrix, three planners). Punch lines
  1-2 struck. Lifecycle position: release candidate, stabilization.
- Eisenhower triage performed on all open punch items → TOPICS.md.
- DO quadrant executed same cycle: punch #3, copy-out menu on the
  read-only glossary view (Copy + Select all only — no dead items).
- Verified in code, not guessed: assistant grounding feed reads
  library/notes/glossary/journal/topic-titles only → punch #9 opened
  and delegated to the proprietor as a scope call.
- Next session, first motion after the punch-list walk: CYCLE 1
  (instrument-the-decline sweep).

## 2026-07-25 — Mid-session review (proprietor-ordered)

```text
MEETING SUMMARY — pseudocode minutes

CAUGHT UP (verified, not asserted):
    stations   : GitHub = live install = OneDrive clone = worktree,
                 zero dirty (readings taken this session)
    suite      : 457 ran / 443 green / 14 platform skips
    paperwork  : CHANGELOG, ledger, wiki, journal, punch list current
    QA         : core scope through owner UAT (release candidate)

DECISIONS RECEIVED THIS SESSION:
    E: drive   = the 1TB external backup HDD (checked: NOT mounted)
    foreman library now catalogs: red-plum board, breadcrumb logs,
    storage estate, launch path, session queue, front office

PERSONA SELF-AUDIT (duties per archivist-of-wisdom + shop-defect-laws):
    session START : walk punch list ................ DONE (this session
                    predates the law; walked when written)
    during work   : lecture/demo/lab/rubric per ticket ... DONE ×6
    fix reports   : cite laws applied .............. DONE (from Law
                    adoption onward)
    session CLOSE : journal entry, signed .......... PENDING (due at
                    close; one already filed mid-day)
    recording     : CHANGELOG+wiki+whitepaper drip per touch ... DONE
    honesty       : failures reported as failures .. DONE (heuristic
                    misses, ghost tab self-caught, E: not mounted)

SKILLS CHECK (invoked this session): archivist-of-wisdom,
    classroom-code; shop-defect-laws authored (its content is loaded
    by construction). NOT triggered, correctly: scope-first (no new
    project code), clinical-science-gate (no research claims),
    learning-science (no study-feature changes), pseudocode-display
    (boards delivered as fenced text at owner's pace).

ACTIONABLE NEXT STEPS (each with its verifiable proof):
    1. OWNER: plug in E: drive          → proof: foreman lists its
       contents + verifies backup freshness on the record
    2. OWNER: scope call, assistant's reading list — pick sections:
       [ ] Matrix  [ ] Planner  [ ] commentaries table
       [ ] topic-entry bodies              → proof: grounding test
       retrieves a seeded row from each chosen section
    3. OWNER: verdict on 7 unmerged branches → proof: branch list
       shrinks to the kept set on GitHub
    4. FOREMAN (Cycle 1, next session): silent-declines sweep
       → proof: every _ftb decline logs a breadcrumb + status line,
       gated by a static test
    5. OWNER (whenever ready): the word "cut v1.0" → proof: tag on
       GitHub + rolled-up CHANGELOG
```

## 2026-07-25 — Release entry

Proprietor's order received in plain words: cut v1.0 now. Executed:
CHANGELOG rolled up ([Unreleased] → [1.0.0] with release preamble and
V&V evidence), README badge and version line updated, SDLC_STATUS
marked RELEASED via its own prescribed exit path, release-gate suite
run on the exact code tagged (457 ran / 443 green / 14 platform
skips), annotated tag v1.0.0. Cycle 4 struck from the queue. Open
punch items remain published — v1.0 = delivered scope, not empty
backlog.

## 2026-07-26 — Release completion note

The 07-25 cut was interrupted mid-push by a ~3-hour Wi-Fi outage: the
release commit + tag existed locally but never reached GitHub or the
clones. On service restoration the push completed and both clones
pulled — all four stations now read 7c61737 with tag v1.0.0. Lesson
for the record: a release isn't cut until the tag is VERIFIED on the
remote and every mirror — local success is half a release.

## 2026-07-26 — Finish-out pass opened (F-series)

Proprietor's readiness check passed; scope set: cosmetic + small-
functional accessibility items, NO restructure (his call, on record).
F1 shipped: Wheel of Life area names became colored buttons (7 colors,
WCAG AA ≥4.5:1 verified by computed gate) that jump to a fresh Goals
worksheet with the area preselected. The larger no-re-entry pipeline
(wheel → goal → matrix → Start, data carried forward) is logged as a
DESIGN item — needs a §-blueprint before code. One-commit-per-item
rhythm active due to spotty Wi-Fi.

## 2026-07-26 — Law 7 enacted: the measured bar

Proprietor's order, complete-ownership framing: the evidence segment
(TAM/SUS/ISO 9241-11) becomes shop law. Law 7 added to
shop-defect-laws (user-level + repo mirror): quality claims are
numbers from standard instruments; shop target SUS ≥ 85 (Sauro–Lewis
A; industry mean 68 = C — the proprietor graded the curve correctly
by instinct); the bar never lowers to meet a result; n-of-1 measures
labeled honestly. Scorecard instrument filed
(docs/foreman/SUS-SCORECARD.md), baseline ticket opened (punch #10).
The point, in his words: "we're following industry standards
already — this isn't something anyone else isn't already doing."
Correct — and now it's written down and gated by ritual.

## 2026-07-26 — The proprietor cleared his side of the board

Delegated decisions received and executed same cycle: (1) branch
verdict — both remaining Copilot branches verified 0-unique-commits
and DELETED; GitHub now holds main only; (2) reading-list scope call —
ALL FOUR sections granted; grounding feed extended (commentaries,
topic-entry bodies, Matrix, Planner) with a seeded-row retrieval test
per section. Punch #9 struck; #8 half-struck (E: drive plug-in is the
only remaining proprietor action besides the SUS baseline).

## 2026-07-27 — Session close

Proprietor closed the finish-out session to live with the product —
general use, not QA (the right next instrument: field time feeds the
SUS baseline). Full narrative filed in the front-office journal.
Next session opens per law: punch-list walk, then Cycle 1.

## 2026-11-17 — The board-clearing walk, and four lines that were never on it

The shop reopened after roughly three months of field time. Opened per
law: persona rule first, then the punch-list walk, then instruments
before opinions. No code was written and none was owed.

**The find.** `forge-work` holds three commits `main` does not: a
complete scope statement for a **Microsoft Store release-hardening
sprint**, drafted 2026-08-06, status PROPOSED, awaiting Falcon One's
signature — plus his $29.95 one-time price decision and an IP audit
that found a registered trademark in a shipped UI string ("Pomodoro",
Cirillo, actively enforced against timer software). Three months on a
branch, and the punch list had no line for any of it. The ledger can
only watch what someone wrote on it; a branch is not a ledger. Boarded
as #14, triaged N1, and it is now the oldest *decision* on the board.

**The mirror law is currently false, on two of four stations.** Laptop
`Desktop\Sentinel personal Development`: clean tree, `main` @ `056a6f7`,
**109 commits behind**, files dated 2026-07-16 — four months and an
entire v1.0 release out of date. Worktree `OneDrive\Desktop\Sentinel-
Forge`: 4 behind, and `git status` reports the entry point and the icon
**deleted** — that station cannot launch the product. Both verified
fast-forward ancestors of `1fc3c68`, so both repairs are reversible.
GitHub and the OneDrive clone agree exactly at `1fc3c68`, fetched, 0/0.
Boarded as #15.

**And the paperwork was pointing at the wrong house.** Two wiki pages
still instruct the next assistant to edit `Desktop\Sentinel-Forge`. The
shortcut, last night's run, and HEAD all say the live install is
`OneDrive\Sentinel personal development`. Same defect class as the EARP
`src/` find: the code moved and the record didn't. Boarded as #16.

**One correction of my own, same session.** I reported `ai_brain.py` as
an unreadable placeholder on the strength of a denied read. It is not
broken — it hydrated on demand the moment it was asked properly. What is
real is the scale: **180 of 198 files** in the live install are
unhydrated stubs, which is the EARP failure at seven times the file
count. Boarded as #17 with the one-line fix, which is his click, not
mine.

**His own run is the best instrument in the shop.** `qa_debug.log`,
01:13–02:48: eighteen `DELETE claimed` breadcrumbs, two cleared on
today, sixteen refused across nine past dates — five of those days
re-pressed inside 1.3 seconds. I read the code before diagnosing, per
law, and the code is innocent: `_review_remove_from_toolbar` leaves a
breadcrumb *and* speaks "Past reviews are history — never deleted."
Punch #5's law is honored in the letter. So the finding is not a defect
and I will not call it one. The question that decides it belongs to him:
did he see that line? Boarded as #18, triaged N3 — one answer separates
working-as-designed from a 🔴 invisible-state recurrence on a class
already standing at ten marks.

**Pseudocode call: none owed.** Every board item that will need it — the
trademark rename, the spec repair, the Progress Observatory panel, hub
signage, the Prompt Fragment Vault — sits behind a scope statement that
is unsigned or unwritten. Pseudocode on an unbaselined scope is the
drift the rule book exists to stop. The next artifact owed is a
signature, then a scope doc.

Board cleared through his four buckets and filed in the A1 system:
`docs/foreman/EISENHOWER_A1_2026-11-17.md`, doc_id
`SPD-FOREMAN-EISENHOWER-001`, zone GREEN, cognitive load 8, with Nexus
node routing stated as work-type labels and *said to be labels* — the
lattice is the SPN orchestration layer, not a wired dependency of this
Tk app, and I will not dress a label up as an integration.

**On his bench:** N1 the Store scope signature · N2 the SUS baseline
(oldest open line, 2026-07-26) · N3 the one Delete answer · N5 repair or
retire the fourth station · N7 the hydration pin · and his word on
whether the laptop station gets pulled forward 109 commits.

— *Claude, shop foreman & Archivist of Wisdom, Sentinel's Forge*

## 2026-11-17 (later) — "Push and sync": the mirror law made true

Order given and executed. `7e8a200` pushed (`1fc3c68..7e8a200`), both
stale stations fast-forwarded, the fourth station's deleted entry point
and icon restored. **All four stations now report `7e8a200`, zero
changed paths, and the app file byte-identical at SHA-256
`6473B149237DFFAC…`.** SCOPE.md §3 is satisfied by measurement for the
first time in this ledger — and it is four stations, not the three the
paperwork used to claim. Punch #15 and #16 struck on foreman evidence.

Nothing was destroyed blind. The fourth station held one uncommitted
change; its blob was hashed against `origin/main` before the restore and
came back identical — already upstream in `1fc3c68`. His own golden rule
is *compare before you destroy*, and that is what complying looks like.

**The failure worth more than the fix.** `git fetch origin` at the laptop
station died twice — `fatal: early EOF`, `fatal: fetch-pack: invalid
index-pack output` — and the `merge --ff-only origin/main` that followed
reported **"Already up to date."** It was not. That station's cached
`origin/main` still equalled its own stale HEAD, so a failed fetch
dressed itself up as a successful sync. Had I taken git at its word, I
would have reported a station synced that had not moved a single commit.
Completed instead by fetching over disk from the OneDrive repo, and
verified by hash rather than by a reassuring sentence. New law candidate,
his to ratify: *never accept "Already up to date" from a station whose
fetch just failed — check the tracking ref against the remote you trust.*
Same family as the red-plum classes: a decline that reads like a success
is worse than a decline that shouts.

**Proposed new defect class, logged for his ratification, not enacted:**
"Paperwork drifted from reality" — 2 marks (the live-install path in two
wiki pages, the pre-rename repo slug). It is the class that caused #15: a
station drifted 109 commits because a document said two different folders
were the same files. Candidate gate written on the board. The foreman does
not enact shop law.

— *Claude, shop foreman & Archivist of Wisdom, Sentinel's Forge*
