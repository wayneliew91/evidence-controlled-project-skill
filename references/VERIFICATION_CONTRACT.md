# Verification Contract

## Evidence standard

Verification claims require direct evidence. Acceptable evidence includes executed tests, deterministic checks, reproducible build output, authoritative artifact comparison, hashes, or other task-appropriate proof.

Do not claim `PASS`, `VERIFIED`, successful migration, successful build, or release readiness from intention, code inspection alone, assumptions, or a worker's unsupported statement.

## Ordinary implementation verification

Verify at least:

1. the authorized changed behavior;
2. directly affected dependencies;
3. relevant frozen capabilities at the dependency boundary;
4. data or output invariants touched by the change.

## Failed verification

When a check fails:

- capture the failure as evidence;
- identify whether the implementation, test, fixture, evidence model, or assumption is wrong;
- do not rewrite authoritative facts merely to satisfy the verifier;
- do not manufacture balancing or placeholder records;
- keep unrelated checks and work moving where safe.

## Truthful status

Use:

- `COMPLETED, NOT VERIFIED` when work exists but evidence is incomplete;
- `BLOCKED` when a required external dependency prevents verification;
- `UNRESOLVED` when evidence conflicts;
- `VERIFIED` only when the defined acceptance checks directly support the claim.

## Verification is not redesign

`VERIFY` mode tests the accepted contract. It does not reopen accepted architecture or frozen behavior simply because another design would be easier to test.
