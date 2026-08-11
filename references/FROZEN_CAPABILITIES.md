# Frozen Capabilities

## Meaning of frozen

`FROZEN` means a capability has an accepted behavior and is closed to unsolicited modification. It may still be covered by regression verification.

Typical reasons:

- previously verified business-critical behavior;
- fragile integration with proven output;
- accepted compatibility contract;
- intentionally stable data lineage;
- completed remediation whose reopening would add risk without new evidence.

## Do not reopen for aesthetics

A cleaner design, newer pattern, smaller implementation, or personal preference is not evidence that a frozen capability should change.

## New evidence

When credible new evidence conflicts with frozen behavior:

1. verify that the evidence actually concerns the same capability and scope;
2. apply the evidence hierarchy;
3. assess whether correctness is materially affected;
4. if yes, classify `REOPEN_RECOMMENDED` and explain the evidence;
5. keep the capability frozen until explicit scoped authorization is granted.

## Scoped reopening

Authorization to reopen one frozen behavior does not unfreeze the whole component. Define the minimum affected contract and regression surface.

## Regression posture

Later work should test frozen capabilities non-invasively when dependency analysis shows they could be affected. A regression failure is evidence to investigate; it is not permission to redesign the capability.
