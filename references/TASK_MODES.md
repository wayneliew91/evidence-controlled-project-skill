# Task Modes

Choose the narrowest mode that satisfies the current request.

## `AUDIT`

Purpose: inspect evidence, compare artifacts, reconstruct history, identify conflicts, and report findings.

Write authority: none.

Default when the user asks to audit, inspect, review, compare, reconcile, investigate, or determine current truth.

## `DESIGN`

Purpose: define intended behavior, interfaces, rules, UI, data contracts, or implementation boundaries from accepted evidence.

Write authority: design artifacts only when explicitly requested; no product implementation by implication.

## `IMPLEMENT`

Purpose: apply explicitly authorized changes to the approved scope.

Write authority: first-level authorized ordinary artifacts only. Protected actions still require second-level authorization.

## `VERIFY`

Purpose: test stated claims and regressions without redesigning the product.

Write authority: none unless a separate implementation authorization exists. A failed test is a finding, not automatic permission to fix.

## `HANDOFF`

Purpose: prepare a bounded execution task for another agent or worker.

A handoff must contain:

- authorized scope;
- evidence authority;
- protected assets;
- frozen capabilities;
- explicit prohibitions;
- acceptance criteria;
- verification commands or evidence requirements;
- unresolved and out-of-scope items.

A handoff transfers instructions, not additional authority.

## `RELEASE`

Purpose: determine whether an accepted implementation is ready to become a release artifact.

Requires cumulative carry-forward regression. Release mode does not itself authorize protected replacement of production/runtime artifacts.
