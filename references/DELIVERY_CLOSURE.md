# Delivery Closure Contract

## Explicit closure mode

Use this contract only when the human has explicitly chosen a delivery/closure strategy and the business/product truth for the release scope is sufficiently frozen.

Closure mode does not weaken correctness. It changes what is allowed to block delivery.

## Release blockers

Treat an item as release-blocking when it materially affects one or more of:

- current product behavior;
- authoritative data integrity;
- required migration/cutover safety;
- build reproducibility or executable integrity;
- security/protected-asset boundaries;
- required current output/export correctness;
- a frozen capability or dependency that the release can regress.

## Non-blocking perfection work

Unless the project profile explicitly elevates them, do not keep delivery open solely for:

- documentation perfection unrelated to current behavior;
- exhaustive dead-code cleanup with no runtime/build impact;
- repeated audit packages that add no new decision evidence;
- stale historical verifiers that assert superseded behavior;
- cosmetic archive cleanup;
- duplicate evidence containers whose lineage is already understood.

Record these as follow-up, archive, or cleanup work rather than silently converting them into release gates.

## One candidate, one closure pass

When closure selects a working source candidate:

1. Freeze the candidate identity.
2. Preserve the previous accepted baseline as comparison evidence.
3. Apply only authorized release-critical fixes to the candidate.
4. Run one cumulative carry-forward regression appropriate to the dependency surface.
5. Compare against the previous accepted baseline for partial reversion or restored obsolete logic.
6. Produce one truthful release status and one cumulative change/carry-forward record.

Do not keep multiple moving candidates alive without a specific experiment that requires them.

## Superseded verifier handling

A failing verifier is not automatically a product blocker. First classify the failure:

- current behavior/data/release invariant is wrong -> blocker;
- verifier encodes superseded truth -> update/deprecate verifier;
- test fixture is stale -> repair fixture;
- evidence is unresolved -> isolate affected scope;
- documentation-only mismatch -> record without blocking unless the release contract requires it.

Never restore an explicitly retired feature merely to make an obsolete verifier green.

## Closure status

Examples of truthful closure language:

- `RELEASE-CRITICAL CHECKS VERIFIED; NON-BLOCKING CLEANUP DEFERRED`
- `BUILD VERIFIED; RELEASE BLOCKER REMAINS`
- `CANDIDATE FROZEN; CUMULATIVE REGRESSION INCOMPLETE`
- `RELEASE READY` only when the project-specific release contract is satisfied.

Protected production/runtime replacement remains separately authorized even after readiness is established.
