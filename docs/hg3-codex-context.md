# HG-3 Codex context

## Current state

- Branch: `hg3-codex`.
- Phase: parameterization started.
- Previous HG-1/HG-2 artifacts and workflows remain untouched.

## Plan

1. Add an isolated `hongguo-crack-audit-v737` workflow with dispatchable sample/version inputs.
2. Parameterize the HG-1 audit scripts so existing invocations remain compatible.
3. Add classes24.dex attribution and `com/b/a` family rescan outputs.
4. Dispatch a full v7.3.7.32 CI run.
5. Render `docs/hg3-diff-report-codex.md` from actual run artifacts and push it.

## Next step

Implement and commit the isolated workflow plus script parameterization, then dispatch CI.
