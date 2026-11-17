# Scope Statement — Store Release Hardening Sprint

> Written per the `scope-first` skill at sprint onset, before any code.
> Status: **BASELINED 2026-11-17 by Falcon One**, with amendments A–D from
> the pre-signature audit folded in. Changes after this are explicit logged
> decisions (one line in `Assistant-Notes.md` §5), never drift.
> Standards frame: ISO/IEC/IEEE 12207 · SWEBOK · IEEE 29148.

_Drafted: 2026-08-06 · Baselined: 2026-11-17 · Owner: Shannon Brian Kelley
(Falcon One) · Foreman: Claude (Falcon Two). Parent baseline:
`docs/SCOPE.md`._

**Amendments at baseline, all four approved by Falcon One 2026-11-17.**
Evidence: `docs/foreman/STORE_SCOPE_PRESIGN_AUDIT_2026-11-17.md`
(`SPD-FOREMAN-STOREAUDIT-001`), which measured every claim in the 2026-08-06
draft against the code.

| # | Amendment | Effect |
|---|---|---|
| **A** | Trademark exposure measured at **one** UI string, not a sweep | §1.6 narrowed to that label + a UI-string-only gate; DB schema and identifier renames moved to §2 |
| **B** | Acceptance A3's app-data half already shipped in `lyceum/db/db_location.py` | A3 re-aimed at the content directories and the `_onedrive_root()` seam |
| **C** | Portability debt sized to one seam + three literals | §1.2 names all four targets so A2's gate has a definition of done |
| **D** | None of the build/certification toolchain is installed | New §1.0 provisioning item added ahead of everything else |

**Sprint-length warning, recorded at baseline:** this is a multi-session
sprint, not housekeeping. Nothing in it is a ten-minute job, and it does not
begin until the general-housekeeping close-out is struck.

**Parent-baseline change this sprint introduces (logged, not drift):**
the app gains a public **distribution channel** (Microsoft Store). The
product itself stays exactly what `SCOPE.md` says — local-first, single
user, no cloud dependency. What changes is that copies now run on
machines that are not this laptop, which is why portability is the heart
of the sprint.

## 1. In scope

0. **Provisioning — Amendment D, added at baseline 2026-11-17, and it goes
   first.** Measured this session: none of `pyinstaller`, `makeappx`,
   `signtool` or `appcert` (WACK) is on PATH. Python 3.13.14 is. Without
   this item, acceptance criteria A1, A4 and A6 are blocked on setup that
   appeared nowhere in the 2026-08-06 draft, and the sprint stalls on its
   first morning. Deliverables: `pip install pyinstaller`; Windows SDK
   installed for `makeappx` / `signtool` / `appcert`; the ≈$19 Microsoft
   individual developer registration completed by the owner; **and a clean
   test machine or VM** — A3's "no Python, no OneDrive, no `sbrya` account"
   condition cannot be met on this laptop, which the draft also did not
   account for.
1. **Build repair** — `Sentinel-Forge.spec` corrected to the real entry
   point (`sentinel_personal_development.py`), bundled-data list audited
   against what actually exists in the repo; a reproducible PyInstaller
   one-folder build.
2. **Portability pass** — no literal `C:\Users\sbrya\...` path anywhere
   in shipped source; every OneDrive-assumed location gains a fallback
   for machines without OneDrive (plain `Documents` / `%LOCALAPPDATA%`);
   a sane first-run on a computer that has never seen this app.
   **Amendment C — the four measured targets, which are the whole job:**
   - `sentinel_personal_development.py:4533` `_onedrive_root()` — today
     returns `os.environ.get("OneDrive") or os.path.expanduser(r"~\OneDrive")`;
     that fallback resolves to a folder that does not exist on a machine
     without OneDrive. **This one seam carries almost all 55 non-comment
     OneDrive call sites** — fix it and the call sites follow.
   - `:107` literal `…\Claude AI\AI_Memory_Core\excerpts`
   - `:108` literal `…\Completed projects\AI_Memory_Core\excerpts`
   - `:118` `DEFAULT_BOOKS_DIR` literal `…\Desktop\Books`

   Pseudocode is due here, on the board via `pseudocode-display`, before
   the first line of it is written. It is the only algorithm work in the
   sprint.
3. **Privacy documentation** — a privacy policy stating the truth the
   code already tells: all processing local, outbound traffic limited to
   user-initiated web search (DuckDuckGo) and optional localhost Ollama;
   microphone audio processed on-device, never transmitted. Reachable at
   a public URL for the Store listing. **Amendment C (mechanism named):**
   GitHub Pages on this repository — free, already owned, no new account.
4. **MSIX packaging** — manifest (identity, capabilities: internet +
   microphone), Store logo assets, the PyInstaller folder wrapped as an
   installable, uninstallable MSIX.
5. **Certification testing** — Windows App Certification Kit run against
   the MSIX; clean-machine test (no Python installed, no OneDrive, no
   `sbrya` account).
6. **IP-clean pass** (added by logged decision, owner's audit order
   2026-08-06) — rename the user-facing "Pomodoro" feature (registered
   trademark, Cirillo, actively enforced against timer software) to a
   generic name ("Focus Cycles"); static gate keeps the mark out of
   shipped UI strings. LICENSE copyright line updated to the owner's
   legal name. Audit found all other content clear: generic templates,
   no bundled third-party text, all dependencies permissively licensed,
   no patent exposure.
   **Amendment A — measured 2026-11-17, and it is one label.** 41
   occurrences of the mark in shipped Python; exactly **one** reaches a
   user: `sentinel_personal_development.py:27877`,
   `tk.Label(dlg, text="Duration (Pomodoro length):")`. That label and the
   UI-string gate are the entire deliverable of this item. The tomato glyph
   at `:516` is in a food-emoji dictionary beside watermelon and carrot —
   unrelated, no action. The 2026-08-06 "no bundled third-party text"
   finding was re-verified: the 1.21 MB `Sentinel Personal Development.txt`
   is the owner's own build-inventory documents and is untracked by git, so
   it is neither in the repository nor in the build.
7. **Store listing & submission** — Partner Center listing at a
   **one-time purchase price of $29.95** (owner's decision, 2026-08-06:
   penetration pricing — undercut the $49.99-lifetime category comps,
   no subscription); honest feature copy (AI assistant worded as
   optional Ollama integration or left off the bullets); submission
   filed by the owner. **Amendment C:** the comps behind the price were
   read on 2026-08-06. The price decision is the owner's and stands; a
   one-line comp re-check happens before the listing goes up, and the
   outcome is logged either way as a decision — not as drift.

## 2. Out of scope (explicit)

- **Renaming database tables, columns, internal identifiers, comments or
  docstrings that contain the trademark** — Amendment A, 2026-11-17.
  `matrix_pomodoros`, `pomodoro_id`, `_pomo_phase`,
  `pomodoro_cycle_log.json` and ~26 comment/docstring mentions stay as they
  are. Two reasons, both load-bearing: none of them is shown to a user, so
  none carries the legal exposure; and `SCOPE.md` §1 commits this project to
  **additive-only migrations** — renaming a live table is not additive, so
  doing it would breach the parent baseline to fix a problem that does not
  exist. The gate asserts over UI strings only.
- **Subscription / Pro tier and all in-app purchases** — ruled out by
  the owner on market evidence (offline chatbots retail at $0; category
  lifetime ceiling $49.99): nothing exists yet with continuing cost;
  parked until a real ongoing service exists.
- **Bundled assistant ("Assistant in the Box")** — legally cleared
  (Ollama MIT; Llama 3.2 Community License permits commercial
  redistribution with license copy + "Built with Llama" display) but
  deferred to its own Phase-2 scoped ticket: embedded llama.cpp engine
  + model in the MSIX (~2GB, well under the Store's 25GB cap), shipped
  as the first Store update. v1 ships with the assistant optional.
- **Android / iOS / smartwatch / smart-ring versions** — separate future
  project behind its own scope-first gate (cross-platform rewrite).
- **New features of any kind** — this sprint changes where the app runs,
  never what it does. Maintenance-mode law holds.
- **Bundling Ollama, Whisper models, or any AI runtime** — they remain
  optional, user-installed, gracefully absent.
- **Auto-update machinery** — the Store's own update channel is the
  mechanism; we build none.
- **Marketing beyond the listing itself.**

## 3. Acceptance criteria (binary, observable)

- **A1** `pyinstaller Sentinel-Forge.spec` completes clean and the
  resulting exe launches on a machine with no Python installed.
- **A2** Static gate added to the suite: shipped source contains no
  literal user-specific path (`sbrya`, hardcoded `C:\Users`); full suite
  green with the gate in it. **Amendment C:** done means the three literals
  at lines 107, 108, 118 are gone and `_onedrive_root()` has a real
  no-OneDrive fallback — the gate asserts those four, not a sentiment.
- **A3** App launched under a Windows account with no OneDrive: starts
  clean, all data lands in `%LOCALAPPDATA%` / local `Documents`, every
  core workflow usable. **Amendment B — half of this is already shipped,
  and it gets credited rather than rebuilt.** `lyceum/db/db_location.py`
  already opens the live database from `%LOCALAPPDATA%\SentinelForge\study.db`
  (deliberately off the cloud-sync path, with the race condition documented
  in its own module docstring), falls back to `~\AppData\Local` when the
  environment variable is absent, snapshots a consistent copy back into the
  synced folder via SQLite's online Backup API, never raises, and has tests
  (`tests/test_db_location.py`). A3 therefore proves out against the
  **content** directories — books, excerpts, Sentinel Documents — and the
  `_onedrive_root()` seam. The app-data half is evidence, not work.
- **A4** MSIX installs, launches, and uninstalls cleanly; WACK report =
  PASS, filed in `docs/build-inventory/`.
- **A5** Privacy policy text matches the code's actual network surface
  (checked line-against-code, clinical-science-gate posture) and is live
  at a public URL.
- **A6** Submission reaches "In certification" in Partner Center.
  **Microsoft's approval is Microsoft's decision** — the sprint's rubric
  ends at a complete, honest submission; publication is not promised.

## 4. Lifecycle target

- Distribution channel maintained for the life of the product
  (`SCOPE.md` horizon: 5–10 years). Each future release rebuilds the
  same spec → MSIX → WACK pipeline; the pipeline is documented well
  enough that a new maintainer could ship a release from the repo alone.
- Account facts, on the record: Microsoft individual developer
  registration ≈ **$19 one-time**; Microsoft signs published packages.
- **Single biggest structural risk, named while cheap:** antivirus /
  certification false-positives against PyInstaller-packed Python apps.
  The seam is already cut: one-folder build, no UPX, and the Store's own
  signing. If certification fails on this, the recorded fallback seam is
  a plain-zip + manifest MSIX layout, not a re-architecture.
