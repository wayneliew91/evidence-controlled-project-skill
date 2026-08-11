# Scope Control

## Authorized scope

Before implementation, be able to state what is authorized to change and what is not. Scope may be defined by files, components, features, records, data ranges, or explicitly named outcomes.

## Out-of-scope discoveries

When a relevant issue is discovered outside current authorization, record it as:

`OUT_OF_SCOPE_FINDING`

Include:

- what was found;
- evidence supporting the finding;
- whether it affects current correctness;
- recommended next action.

Do not silently implement it.

## Dependency exception

If an out-of-scope defect directly prevents the authorized task from being correct, classify it as a blocking dependency. Explain the minimum scope expansion required. Do not treat dependency discovery as self-authorization.

## Avoid collateral refactoring

Do not use an authorized change as an excuse to:

- redesign adjacent components;
- normalize unrelated naming;
- replace working architecture;
- remove unfamiliar code solely because it appears unused;
- “clean up while here” outside the required dependency surface.

## Non-blocking unresolved work

An `UNRESOLVED` item freezes only its dependency cone. Continue unrelated authorized work when it can be completed without assuming the disputed fact.

## Completion accounting

At delivery, separate:

- completed authorized changes;
- verified changes;
- blocked items;
- unresolved items;
- deferred items;
- out-of-scope findings.

Do not collapse these categories into a single “done” status.
