# Release Contract

## Release is cumulative

A release is not validated only by tests for the newest change. Before release readiness can be claimed, perform **Cumulative Carry-Forward Regression** over accepted behavior that could be affected by the release.

## Carry-forward register

Maintain or reconstruct a register containing, as applicable:

- accepted requirements;
- previously fixed regressions;
- frozen capabilities;
- naming and compatibility contracts;
- critical data/output invariants;
- protected boundaries;
- accepted migrations or historical corrections;
- explicit supersessions.

## Release checks

1. Verify the current authorized change.
2. Identify direct and transitive dependency surfaces.
3. Run relevant regression checks against carry-forward items.
4. Compare the candidate against the previous accepted baseline when a baseline exists.
5. Flag partial reversion, renamed behavior, missing functionality, or restored obsolete logic.
6. Confirm unresolved or deferred items are represented honestly in release notes/status.
7. Verify release artifacts from direct build/output evidence.

## Release result

Use `RELEASE READY` only when required checks support it.

If the candidate is technically built but cumulative regression is incomplete, report the narrower truth, for example: `BUILD VERIFIED; RELEASE REGRESSION INCOMPLETE`.

## Protected release actions

Determining readiness and replacing a formal release/runtime are distinct actions. Replacement of protected release artifacts still requires the authorization defined in [PROTECTED_ASSETS.md](PROTECTED_ASSETS.md).
