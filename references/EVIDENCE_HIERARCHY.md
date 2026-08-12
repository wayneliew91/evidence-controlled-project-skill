# Evidence Hierarchy

## Default rank

Use this default authority order for the same disputed fact or behavior:

1. Latest explicit human decision for the same scope.
2. Accepted specification, policy, or business truth.
3. Accepted and verified implementation baseline **for implemented behavior**.
4. Primary source evidence.
5. Derived, consolidated, transformed, or generated evidence.
6. Historical, rejected, superseded, or exploratory material.

A project profile may refine this ranking when domain rules require it. Any inversion of normal source lineage must be explicit.

## Authority is fact-specific

Do not ask “which file is highest?” without first asking “authority for what fact?”

- A signed invoice/claim/statement may be stronger evidence of a historical transaction than application code.
- A verified accepted release may be stronger evidence of the behavior users actually received than an exploratory design note.
- A bank record may be authoritative for settlement date/amount/channel but not for the business meaning of the underlying claim.
- A current explicit human ruling may define future/current product behavior while leaving historical source records immutable.

The same artifact can be strong evidence for one fact and weak evidence for another.

## Conflict decision sequence

Do not choose a winner from rank alone. Evaluate, in order:

1. **Fact scope** — what exact fact/behavior is disputed?
2. **Rank** — which evidence class is normally authoritative for that fact?
3. **Acceptance** — was the artifact or decision explicitly accepted, rejected, provisional, or merely generated?
4. **Lineage** — is it primary, copied, transformed, consolidated, migrated, or derived?
5. **Time** — was it created before or after the disputed state?
6. **Explicit supersession** — does authoritative evidence clearly state that an older rule or artifact is replaced?

## Recency is not authority

A newer export, summary, migration output, cache, generated report, or consolidated workbook does not automatically override an older primary record.

Likewise, an older accepted specification does not automatically defeat a newer explicit human decision for the same scope.

## Current truth vs historical truth

A current decision can retire a feature or rename/reclassify a current business concept without rewriting historical evidence. Keep two questions separate:

- What was recorded/happened historically?
- What is the accepted current product/business rule now?

Do not keep obsolete current behavior alive merely because historical evidence contains it, and do not rewrite history merely because the current rule changed.

## Unresolved conflict

If the sequence above cannot establish a defensible answer:

- classify the disputed scope `UNRESOLVED`;
- preserve both sides of the evidence chain;
- do not invent a compromise value;
- do not modify authoritative data merely to remove the conflict;
- continue independent work that does not depend on the unresolved decision.

## Supersession record

When one source legitimately supersedes another, record at least:

- superseded item;
- superseding item or decision;
- affected scope;
- reason;
- effective date or ordering evidence where relevant;
- whether historical evidence remains immutable;
- which current code/UI/test/report surfaces must stop depending on the superseded rule.
