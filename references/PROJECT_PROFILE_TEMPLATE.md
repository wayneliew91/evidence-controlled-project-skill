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
├── CURRENT_TRUTH.md
├── EVIDENCE.md
├── EVIDENCE_REGISTER.md
├── DEPENDENCIES.md
├── FROZEN_CAPABILITIES.md
├── PROTECTED_ASSETS.md
├── RELEASE_CONTRACT.md
└── CLOSURE.md
```

These may be separate files or equivalent sections in a smaller profile.

## `PROFILE.md`

Define:

- profile identifier;
- project purpose;
- current accepted phase;
- local terminology;
- active task boundaries;
- explicit generic-rule overrides, if any.

## `BASELINE.md`

Define accepted technical/product baselines, supported platforms, canonical source location policy, architecture constraints, abandoned routes that are evidence-only, and the current working-candidate policy.

## `CURRENT_TRUTH.md`

Maintain the current accepted business/product rules and explicit supersessions. For each high-risk supersession record:

- current rule;
- superseded rule/artifact;
- effective ordering/date evidence;
- affected UI/data/logic/report/test surfaces;
- historical-preservation requirement, if any.

This prevents stale specs/tests from silently restoring retired behavior.

## `EVIDENCE.md`

Define project-specific evidence ranks, primary sources, accepted specifications, known derivatives, superseded artifacts, source-system identifiers, and lineage rules.

## `EVIDENCE_REGISTER.md`

Define the project’s evidence-index schema and where the authoritative register lives. Include source/provider IDs, artifact lineage, duplicate/version relationships, canonical mappings, review state, and unresolved fields. The register indexes originals; it does not replace them.

## `DEPENDENCIES.md`

Define module/service dependency boundaries, especially:

- which module owns each economic/business event;
- which modules only settle, allocate, map, or report it;
- frozen integration/link contracts;
- dependency-first reconstruction order for any damaged core.

## `FROZEN_CAPABILITIES.md`

List capability identifiers, accepted behavior, verification evidence, freeze reason, and regression expectations.

## `PROTECTED_ASSETS.md`

List project-local production/runtime/data/release boundaries, credential/secret exclusions, and any stricter handling requirements.

## `RELEASE_CONTRACT.md`

List project-specific carry-forward checks, acceptance commands, required artifacts, current output/data invariants, and release-safety requirements.

## `CLOSURE.md`

When delivery-first closure is explicitly authorized, define:

- chosen working candidate;
- release-critical blockers;
- non-blocking cleanup/deferred work;
- previous accepted baseline for comparison;
- cumulative regression scope;
- protected cutover/replacement actions that still require separate authorization.

## Override rule

A profile may specialize generic behavior only through an explicit statement such as:

```text
OVERRIDE: <generic rule>
PROJECT RULE: <replacement rule>
RATIONALE: <accepted authority>
```

Silence is not an override.

See the [generic example profile](../examples/generic-project-profile/PROFILE.md).
