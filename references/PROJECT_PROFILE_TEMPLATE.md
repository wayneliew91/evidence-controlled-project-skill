# Project Profile Template

A project profile supplies local facts without changing the generic governance model.

## Activation

Use hybrid activation:

- If the active project is unambiguous from explicit user wording or local project context, load its profile automatically.
- If multiple profiles may apply, do not guess. Keep generic rules active until profile identity is resolved.
- Never infer a project profile solely from a coincidental filename or unrelated historical reference.

## Recommended profile structure

```text
project-profile/
├── PROFILE.md
├── BASELINE.md
├── EVIDENCE.md
├── FROZEN_CAPABILITIES.md
├── PROTECTED_ASSETS.md
└── RELEASE_CONTRACT.md
```

## `PROFILE.md`

Define:

- profile identifier;
- project purpose;
- current accepted phase;
- local terminology;
- active task boundaries;
- explicit generic-rule overrides, if any.

## `BASELINE.md`

Define accepted technical/product baselines, supported platforms, canonical source location policy, architecture constraints, and abandoned routes that are evidence-only.

## `EVIDENCE.md`

Define project-specific evidence ranks, primary sources, accepted specifications, known derivatives, superseded artifacts, and lineage rules.

## `FROZEN_CAPABILITIES.md`

List capability identifiers, accepted behavior, verification evidence, freeze reason, and regression expectations.

## `PROTECTED_ASSETS.md`

List project-local production/runtime/data/release boundaries and any stricter handling requirements.

## `RELEASE_CONTRACT.md`

List project-specific carry-forward checks, acceptance commands, required artifacts, and release invariants.

## Override rule

A profile may specialize generic behavior only through an explicit statement such as:

```text
OVERRIDE: <generic rule>
PROJECT RULE: <replacement rule>
RATIONALE: <accepted authority>
```

Silence is not an override.

See the [generic example profile](../examples/generic-project-profile/PROFILE.md).
