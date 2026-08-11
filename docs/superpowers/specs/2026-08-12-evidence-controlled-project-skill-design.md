# Evidence-Controlled Project Skill — Design Specification

## Purpose

Create an agent-agnostic project-governance skill for evidence-heavy software and operational projects. The skill must be reusable across organizations and projects without embedding company names, customer names, private paths, amounts, credentials, or project-specific history.

## Core posture

The default state is `AUDIT / READ_ONLY`. An agent may inspect, compare, reconcile, classify, and report without write authority. Ordinary implementation requires an explicit first-level authorization. Protected actions require a separate second-level authorization.

## Task modes

The skill defines six modes: `AUDIT`, `DESIGN`, `IMPLEMENT`, `VERIFY`, `HANDOFF`, and `RELEASE`. If the user does not name a mode, the agent chooses the narrowest mode supported by the request. Evidence-first review defaults to `AUDIT`.

## Authorization model

Four operational states govern write authority:

1. `READ_ONLY`
2. `IMPLEMENT_AUTHORIZED`
3. `PROTECTED_ACTION_PENDING`
4. `PROTECTED_ACTION_AUTHORIZED`

A protected action may not be inferred from general implementation approval. Protected actions include destructive deletion, irreversible migration, production/runtime mutation, historical-record overwrite, release-artifact replacement, credential/secret handling, and copying sensitive data outside its approved boundary.

## Project profile activation

Use a hybrid activation model. Load a project profile automatically when the current project is unambiguous from local project context or explicit user wording. When multiple profiles could match, do not guess; keep generic rules active and resolve the profile before applying project-specific constraints.

Project profiles contain only project-local rules. The public generic example must remain synthetic and organization-neutral.

## Evidence conflict resolution

Resolve conflicts using this decision order:

1. Evidence rank.
2. Acceptance status.
3. Source lineage (primary vs derived).
4. Time.
5. Explicit supersession.

A newer derived artifact does not automatically override an older primary source. If the conflict remains unresolved, classify it as `UNRESOLVED`; freeze only the affected scope and continue independent work.

## Evidence hierarchy

Default hierarchy:

1. Latest explicit human decision for the same scope.
2. Accepted specification / business truth.
3. Accepted and verified baseline.
4. Primary source evidence.
5. Derived / consolidated evidence.
6. Historical / superseded material.

Project profiles may refine the hierarchy but may not silently invert primary-versus-derived lineage without an explicit project rule.

## Scope control

Authorization is scope-bound. Discoveries outside the current scope are recorded as `OUT_OF_SCOPE_FINDING` and are not silently implemented. If an out-of-scope issue directly prevents correctness of the authorized task, identify the dependency and obtain expanded authorization before changing it.

## Frozen capability model

A `VERIFIED` or `FROZEN` capability is not reopened because a different implementation appears cleaner. New evidence may produce `REOPEN_RECOMMENDED`, but the capability remains frozen until the user explicitly authorizes a scoped reopening.

## Validation model

Ordinary implementation: verify the changed scope and directly affected dependencies.

Release: run cumulative carry-forward regression against all accepted requirements, frozen capabilities, naming contracts, and previously accepted behavior that can be affected by the release.

No agent may claim `PASS`, `VERIFIED`, build success, migration success, or release readiness without direct evidence from executed checks or authoritative artifacts.

## Status vocabulary

Use the following status terms consistently:

- `COMPLETED`
- `VERIFIED`
- `FROZEN`
- `BLOCKED`
- `UNRESOLVED`
- `DEFERRED`
- `OUT_OF_SCOPE_FINDING`
- `REOPEN_RECOMMENDED`

## Backup and protected data rules

Non-destructive working backups of ordinary source/configuration files are allowed when useful for rollback. Production data, runtime state, credentials, secrets, regulated data, and sensitive business data must not be copied, exported, or uploaded merely to create convenience backups. Their handling follows the protected-asset boundary and requires the appropriate authorization.

## Agent portability

The core skill is runtime-neutral. Adapter files explain how ChatGPT, Codex, Claude, and generic agents should map their available tools to the same rules without duplicating the governance model.

## Repository shape

- `SKILL.md` — concise discovery and execution entrypoint.
- `references/` — detailed governance contracts.
- `adapters/` — runtime-specific loading/tool guidance only.
- `examples/generic-project-profile/` — synthetic profile with no real business identifiers.
- `tests/` — pressure scenarios and validation documentation.
- `scripts/validate_skill.py` — structural, link, frontmatter, and privacy checks.
- `docs/superpowers/` — design and implementation plan provenance.

## Privacy requirement

The repository must not contain real company/project/customer names, private filesystem paths, real account identifiers, credentials, personal contact details, or private business amounts. All examples must be synthetic.
