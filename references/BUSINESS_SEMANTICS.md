# Business Semantics Contract

## Canonical identity vs source labels

Separate the business entity from the label captured by a source artifact.

- Canonical identity uses a stable internal key and the currently accepted display name.
- Historical names, aliases, abbreviations, former names, and source labels remain traceability metadata.
- A historical label does not create a new entity, project, account, or category unless independent evidence proves one exists.
- Historical transaction snapshots may preserve the original label even after the master identity changes.

Avoid name-string joins when stable IDs or explicit mappings exist.

## Transaction meaning comes from transaction evidence

Do not infer business semantics from a nearby but weaker event.

Examples of the generic rule:

- Bank/settlement evidence can prove payee, amount, date, and channel; it does not automatically prove the underlying claim/payment type.
- Sequence numbers such as “Claim 7” do not automatically determine `Advance`, `Progress`, or `Final` meaning.
- A common historical pattern does not become a current default without an explicit accepted rule.

When transaction type is not supported by authoritative evidence, keep it unclassified rather than guessing.

## One economic event, one owner

Cross-module records may describe different stages of the same economic event. Define which event creates value/cost and which events only settle, allocate, classify, or report it.

Typical invariant:

```text
source document -> economic event
settlement       -> liability/receivable/cash state change
report           -> derived presentation
```

Do not create a second revenue/cost merely because settlement or reporting occurs in another module.

## Typed adjustments stay typed

Do not collapse materially different source adjustments merely to simplify the data model. Preserve source meaning at backend/evidence level, such as:

- material deduction;
- previous advance applied;
- discount;
- labour or service supplied by another party;
- retention;
- omission/variation;
- other source-specific adjustments.

A simple UI may summarize these concepts, but source semantics, amount lineage, and auditability must remain reconstructable.

## Defaults are decisions

A dropdown default is safe only when the value is a fixed fact or an explicit current rule authorizes the default. Do not preselect a business decision because it is common, historical, convenient, or present in an old master record.

Use a neutral placeholder when the user/evidence must decide the value.

## Retired concepts

When an authoritative current decision explicitly retires a feature, category, name, or business concept:

- remove it from active current behavior, normal UI, selectable values, current rules, and current regression anchors;
- update stale tests/verifiers/specs that incorrectly require it;
- preserve original historical evidence only where traceability or immutable records require it;
- do not keep the retired concept alive as hidden current logic “for compatibility” unless an explicit compatibility contract requires that behavior.
