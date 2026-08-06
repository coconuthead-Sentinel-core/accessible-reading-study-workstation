# Scope Statement — Store Release Hardening Sprint

> Written per the `scope-first` skill at sprint onset, before any code.
> Status: **PROPOSED — awaiting Falcon One sign-off.** On sign-off this
> becomes the sprint baseline; changes after that are explicit logged
> decisions (one line in `Assistant-Notes.md` §5), never drift.
> Standards frame: ISO/IEC/IEEE 12207 · SWEBOK · IEEE 29148.

_Drafted: 2026-08-06 · Owner: Shannon Brian Kelley (Falcon One) ·
Foreman: Claude (Falcon Two). Parent baseline: `docs/SCOPE.md`._

**Parent-baseline change this sprint introduces (logged, not drift):**
the app gains a public **distribution channel** (Microsoft Store). The
product itself stays exactly what `SCOPE.md` says — local-first, single
user, no cloud dependency. What changes is that copies now run on
machines that are not this laptop, which is why portability is the heart
of the sprint.

## 1. In scope

1. **Build repair** — `Sentinel-Forge.spec` corrected to the real entry
   point (`sentinel_personal_development.py`), bundled-data list audited
   against what actually exists in the repo; a reproducible PyInstaller
   one-folder build.
2. **Portability pass** — no literal `C:\Users\sbrya\...` path anywhere
   in shipped source; every OneDrive-assumed location gains a fallback
   for machines without OneDrive (plain `Documents` / `%LOCALAPPDATA%`);
   a sane first-run on a computer that has never seen this app.
3. **Privacy documentation** — a privacy policy stating the truth the
   code already tells: all processing local, outbound traffic limited to
   user-initiated web search (DuckDuckGo) and optional localhost Ollama;
   microphone audio processed on-device, never transmitted. Reachable at
   a public URL for the Store listing.
4. **MSIX packaging** — manifest (identity, capabilities: internet +
   microphone), Store logo assets, the PyInstaller folder wrapped as an
   installable, uninstallable MSIX.
5. **Certification testing** — Windows App Certification Kit run against
   the MSIX; clean-machine test (no Python installed, no OneDrive, no
   `sbrya` account).
6. **Store listing & submission** — Partner Center listing at a
   **one-time purchase price** (owner sets the number); honest feature
   copy (AI assistant worded as optional Ollama integration or left off
   the bullets); submission filed by the owner.

## 2. Out of scope (explicit)

- **Subscription / Pro tier and all in-app purchases** — nothing exists
  yet with continuing cost; parked until a real ongoing service exists.
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
  green with the gate in it.
- **A3** App launched under a Windows account with no OneDrive: starts
  clean, all data lands in `%LOCALAPPDATA%` / local `Documents`, every
  core workflow usable.
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
