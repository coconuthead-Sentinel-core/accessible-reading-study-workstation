# Pre-signature Audit — Store Release Hardening Scope

```yaml
doc_id: SPD-FOREMAN-STOREAUDIT-001
title: Pre-signature audit of docs/SCOPE_STORE_RELEASE.md, measured against the code
zone: GREEN
cognitive_load: 7
timestamp: 2026-11-17T00:00:00Z
status: ACTIVE
author: Claude, shop foreman (Falcon Two), for Falcon One's signature
version: v001
naming: SPD-FOREMAN-store_scope_presign_audit_2026-11-17_v001
audited_document: docs/SCOPE_STORE_RELEASE.md @ forge-work 3bdfa34 (108 lines)
triage_item: N1 / punch #14
```

Falcon One selected N1. The scope was drafted **2026-08-06** and has not
been touched since. Before a signature baselines it, the foreman measured
every claim in it against the code as it stands today — because a scope
signed against stale facts is drift with a signature on it.

**Nothing below changes the scope.** Amendments are marked **PROPOSED** and
wait on his word. `scope-first` §4: scope changes are explicit logged
decisions, and only the owner makes them.

---

## 1. What held up

| Scope claim | Verdict |
|---|---|
| §1.1 the spec names the wrong entry point | ✅ **CONFIRMED.** `Sentinel-Forge.spec` line 37: `Analysis(["book_reader.py"])` — a file this repo does not contain. A1 cannot pass today. |
| §1.1 bundled-data list needs auditing | ✅ Audited, and it is **clean**: the spec bundles `sentinel.ico` and the `tts/` tree only. No docs, no journals, no personal paperwork reach the package. |
| IP audit: "no bundled third-party text" | ✅ **RE-VERIFIED.** The one suspicious artifact — `Sentinel Personal Development.txt`, 1.21 MB — is a concatenation of **his own** build-inventory documents, and it is **untracked by git**. It is not in the repo and not in the build. The August audit was right. |
| §4 PyInstaller false-positive risk | ✅ Still the correct call-out. One-folder, no UPX, Store signing — seam already cut. |

## 2. What the measurements changed

### 2.1 The trademark item is far smaller than it reads

41 occurrences of the mark in shipped Python. Broken down:

| Where | Count | Reaches a user? |
|---|---:|---|
| **UI string** — `sentinel_personal_development.py:27877`, `tk.Label(dlg, text="Duration (Pomodoro length):")` | **1** | **YES — this is the whole user-facing exposure** |
| Comments and docstrings | 5 + ~21 | No |
| Internal identifiers (`_pomo_phase`, `_matrix_pomodoro_id`) | — | No |
| **DB schema names** (`matrix_pomodoros` table, `pomodoro_id` column) | several | No |
| `pomodoro_cycle_log.json` (data file name) | 1 | On disk only |

The tomato glyph at line 516 is in a food-emoji dictionary
(`"watermelon", "pineapple", "tomato", "carrot"`) and has nothing to do
with the timer. No action.

> **PROPOSED AMENDMENT A — narrow §1.6.** Rename the one UI label; put the
> static gate over **UI strings only**. Declare **explicitly out of scope**:
> renaming DB tables and columns, internal identifiers, comments and
> docstrings. Reason, and it is a law not a preference: `SCOPE.md` §1 commits
> this project to **additive-only migrations**, and renaming
> `matrix_pomodoros` is not additive. The legal exposure is the mark shown to
> a user, which is one label and about ten minutes of work.

### 2.2 Acceptance criterion A3 is already half-built

`lyceum/db/db_location.py` exists and already does what A3 asks: it opens
the live database from `%LOCALAPPDATA%\SentinelForge\study.db` — explicitly
*off* the cloud-sync path — falls back to `~\AppData\Local` when the
environment variable is missing, snapshots a consistent copy back into the
synced folder via SQLite's online Backup API, and never raises. There is a
test file for it (`tests/test_db_location.py`).

> **PROPOSED AMENDMENT B — re-aim A3.** The app-data half is shipped and
> tested; say so, and credit it. Re-aim A3 at what is actually unproven: the
> **content** directories (books, excerpts, Sentinel Documents) and the
> `_onedrive_root()` seam on a machine with no OneDrive.

### 2.3 The portability debt is concentrated, not scattered

82 `OneDrive` hits across 7 files reads like a sweep. It is not. Almost all
of them route through **one seam**, `_onedrive_root()`
(`sentinel_personal_development.py:4533`), which returns
`os.environ.get("OneDrive") or os.path.expanduser(r"~\OneDrive")`. On a
machine without OneDrive that fallback resolves to a folder that does not
exist. Fix the seam, and the call sites follow.

Outside the seam there are exactly **three** hardcoded user paths:

| Line | Literal |
|---:|---|
| 107 | `C:\Users\sbrya\OneDrive\Desktop\Claude AI\AI_Memory_Core\excerpts` |
| 108 | `C:\Users\sbrya\OneDrive\Desktop\Claude AI\Completed projects\AI_Memory_Core\excerpts` |
| 118 | `DEFAULT_BOOKS_DIR = C:\Users\sbrya\OneDrive\Desktop\Books` |

> **PROPOSED AMENDMENT C — give A2 a definition of done.** Name the four
> targets in §1.2: the three literals above plus `_onedrive_root()`'s
> fallback. A2's static gate then has something precise to assert, instead of
> "no literal user-specific path anywhere", which is a goal, not a test.

### 2.4 The toolchain the sprint needs is not installed

| Tool | Needed by | Present |
|---|---|---|
| `pyinstaller` | A1 | ❌ not on PATH |
| `makeappx` | A4 | ❌ not on PATH (Windows SDK) |
| `signtool` | A4 | ❌ not on PATH (Windows SDK) |
| `appcert` (WACK) | A4 | ❌ not on PATH (Windows SDK) |
| Python | all | ✅ 3.13.14 |

> **PROPOSED AMENDMENT D — add §1.0, provisioning.** `pip install
> pyinstaller`, install the Windows SDK for `makeappx` / `signtool` /
> `appcert`, and the ≈$19 individual developer registration. As written,
> A1, A4 and A6 are blocked on setup that appears nowhere in the plan — the
> sprint would stall on its first morning.

### 2.5 Two smaller notes

- **§1.3 privacy policy "reachable at a public URL"** names no mechanism.
  GitHub Pages on this repo is the cheapest honest one and costs nothing.
  *PROPOSED: name it, so A5 is executable.*
- **§1.7 pricing comps are three months old.** His $29.95 decision is his
  and the foreman is not re-opening it. But the comps it was reasoned
  against were read on 2026-08-06. *PROPOSED: a one-line comp re-check
  before the listing goes up, logged either way as a decision.*

## 3. Honest statement of what was NOT checked

- **The suite was not run.** README claims 536 tests (`e764e80`,
  2026-08-23). Still documented, still not demonstrated — triage N8, and it
  is the gate ahead of the first code change in this sprint.
- **No clean-machine test was performed.** A3's "no Python, no OneDrive, no
  `sbrya` account" condition cannot be met on this laptop. It needs a second
  machine or a VM, which is itself unprovisioned — a sizing fact the scope
  does not mention.
- **Market and legal facts were re-read from the scope, not re-researched.**
  The trademark status of the mark, the Store's fee and the $19 figure are
  as the August audit recorded them. If his signature rests on any of those,
  they get verified first — `clinical-science-gate` posture applies to legal
  and market claims the same way it applies to clinical ones.

## 4. The foreman's recommendation

**Sign it, with amendments A–D folded in first.** The scope is sound work:
its structure is right, its out-of-scope list is disciplined, and its
single named structural risk is the correct one. Measurement moved it in the
owner's favour on the two items that looked worst — the trademark exposure
is one label, and the data-location criterion is already mostly shipped —
and against him on one he had not accounted for: none of the build and
certification toolchain is installed.

The first artifact after signature is **not pseudocode**. It is the spec
repair and the toolchain install, neither of which is algorithm work.
Pseudocode comes due at §1.2, the portability seam, and goes on the board
via `pseudocode-display` before a line of it is written.

— *Claude, shop foreman & Archivist of Wisdom, Sentinel's Forge*
