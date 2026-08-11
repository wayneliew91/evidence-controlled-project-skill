---
name: evidence-controlled-project
description: Use when auditing, designing, implementing, verifying, handing off, or releasing an evidence-heavy project where source authority, conflicting records, protected assets, frozen behavior, or scope control matter.
---

# Evidence-Controlled Project

## Core principle

Treat the project as an evidence-controlled system, not a greenfield rewrite. Default to `AUDIT / READ_ONLY`; preserve accepted truth, keep authorization scope-bound, and never manufacture consistency merely to finish a task or satisfy a verifier.

## Start here

1. Resolve the narrowest task mode: `AUDIT`, `DESIGN`, `IMPLEMENT`, `VERIFY`, `HANDOFF`, or `RELEASE`.
2. Load a project profile automatically only when the active project is unambiguous. If profile identity is ambiguous, keep generic rules active and do not guess project-specific constraints.
3. Read the references relevant to the task:
   - [Core principles](references/CORE_PRINCIPLES.md)
   - [Authorization model](references/AUTHORIZATION_MODEL.md)
   - [Evidence hierarchy](references/EVIDENCE_HIERARCHY.md)
   - [Task modes](references/TASK_MODES.md)
   - [Scope control](references/SCOPE_CONTROL.md)
   - [Protected assets](references/PROTECTED_ASSETS.md)
   - [Frozen capabilities](references/FROZEN_CAPABILITIES.md)
   - [Verification contract](references/VERIFICATION_CONTRACT.md)
   - [Release contract](references/RELEASE_CONTRACT.md)

## Authorization boundary

Ordinary implementation requires explicit scoped authorization. General implementation approval does **not** authorize protected actions. When a protected action becomes necessary, set `PROTECTED_ACTION_PENDING`, explain the exact action and impact, and require separate explicit authorization before performing it.

Authorization expires with the approved scope. Finishing one authorized change does not create standing write permission.

## Evidence conflicts

Resolve conflicts by evidence rank, acceptance status, source lineage, time, then explicit supersession. Recency alone is not authority. If evidence still conflicts, mark only the affected scope `UNRESOLVED` and continue independent work.

## Scope and frozen behavior

Record unrelated discoveries as `OUT_OF_SCOPE_FINDING`; do not silently implement them. A verified or frozen capability stays closed unless evidence demonstrates a correctness conflict. Even then, mark `REOPEN_RECOMMENDED`; modification still requires explicit scoped authorization.

## Verification truthfulness

Never claim `PASS`, `VERIFIED`, successful build, migration, or release readiness without direct evidence. Never alter authoritative data or invent balancing records merely to make validation pass.

For ordinary changes, verify the authorized scope and affected dependencies. For `RELEASE`, apply cumulative carry-forward regression from the release contract.

## Project profiles

Use [PROJECT_PROFILE_TEMPLATE.md](references/PROJECT_PROFILE_TEMPLATE.md) for project-local rules. Profiles may specialize the generic contract but must identify any intentional override explicitly.
