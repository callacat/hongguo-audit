# HG-3b Codex context

## Status
- Branch HEAD after sync: `8504421` / `f2f0a4ebab3fae316bfd4ab94c0c86aab79fff72`.
- Evidence source: CI run `34888317725`.
- Scope: only the `classes14/com/tencent/tinker/loader/MuteApplication.smali` `init()` invocation; A/B/D remain unchanged.

## Steps

1. Added isolated `.github/workflows/hongguo-clean-build-v737-codex.yml` and `scripts/hg3b_patch_entry.py`.
2. Enforced sample hashes, inner `assets/base.apk` SHA-256, signed APK reparsing, NOP retention, and zero external `com/b/a` references.
3. Publishes `hongguo-v7.3.7.32-clean-rN-codex.apk` with build evidence to `docs/hg3b/`.

## Trigger fix

- Added push trigger limited to this workflow path; first push only indexed `workflow_dispatch` and did not start a run.

## Run 34897088857

- Failure: push event did not populate dispatch inputs; workflow env defaults were absent, so sample download found no assets.
- Fix: restore v737 default asset names and SHA-256 values when inputs are empty.

## Run 34897196400

- Gate 1 passed with inner base.apk SHA-256 `a49cf486fb6c96d7b9169b3fa6a4a020295a8e46b78949b6b30fadc29b955bf9`.
- Failure: patch path mistakenly looked for `smali_classes4`; corrected to the audited `smali_classes14` entry.

## Run 34897535552

- Patch succeeded at `smali_classes14/com/tencent/tinker/loader/MuteApplication.smali` line 1129 (`HG3B_PATCH_DONE files=1 invokes=1`).
- Failure: family retention checks mistakenly looked under `classes14`; audit lists `com/b/a`, `com/b/a$Android_id`, and `com/b/a$Reflect` under `classes23`.
- Fix: moved family retention checks to `smali_classes23`.

## Run 34898121625

- Passed: build, zipalign, apksigner v1/v2/v3, signed inner base.apk SHA-256 gate, and dex count 24.
- Failure: reparsing did not preserve the smali comment marker, so the gate could not observe the NOP.
- Fix: emit an explicit `nop-void` and assert exactly one NOP within `onCreate()V` after reparse.

## Run 34898868567

- Build rejected `nop-void` smali syntax (`mismatched input`).
- Fix: use smali `nop` opcode instead.

## Run 34899099802

- Build and signature gates passed; reparse failed because the NOP gate did not import `re`.
- Fix: import `re` in the reparsing gate.

## Run 34899654207

- All build gates passed and Release `hg3b-codex-r1` was created.
- Asset: `hongguo-v7.3.7.32-clean-r1-codex.apk`; size `277643531`; SHA-256 `03e07aa4940e1afcc3b146a5079ac0eb47fc60c6718f153d09ae699f87913ea6`.
- Failure was only evidence copy: apktool renamed the diff target to `MuteApplication_original.diff`; switched to reading any `*.diff` in the point-diff directory.

## Run 34900211353

- All build gates passed; Release `hg3b-codex-r4` created.
- Asset: `hongguo-v7.3.7.32-clean-r4-codex.apk`; size `277643531`; SHA-256 `033f89e00ef0c211ac82ac5b6cd53db5f98a6aa1edec1b3c5d585986d1b929d1`.
- Failure was evidence copy path: `hg3b-point-diff` is under `work/`; corrected.

## Final success

- Run `34900712742` completed with conclusion `success`.
- Evidence commit returned by CI: `6f7f5d2`.
- Final Release: `hg3b-codex-r5`; asset `hongguo-v7.3.7.32-clean-r5-codex.apk`; size `277643531`; SHA-256 `64d47684adf515df05c151492fda3d2feff7f2f0315a602fe48b1fd061cb5685`.
- Final report: `docs/hg3b-report-codex.md`.
