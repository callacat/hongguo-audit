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
