---
name: evidence-controlled-project
description: Use when auditing, designing, implementing, verifying, handing off, reconstructing, or releasing an evidence-heavy project where source authority, conflicting records, protected assets, frozen behavior, business semantics, or scope control matter.
---

# Evidence-Controlled Project

## Core principle

Treat the project as an evidence-controlled system, not a greenfield rewrite. Default to `AUDIT / READ_ONLY`; preserve accepted truth, keep authorization scope-bound, and never manufacture consistency merely to finish a task or satisfy a verifier.

## Start here

1. Resolve the narrowest task mode: `AUDIT`, `DESIGN`, `IMPLEMENT`, `VERIFY`, `HANDOFF`, or `RELEASE`.
2. Load a project profile automatically only when the active project is unambiguous. If profile identity is ambiguous, keep generic rules active and do not guess project-specific constraints.
3. Read only the references relevant to the task:
   - [Core principles](references/CORE_PRINCIPLES.md)
   - [Authorization model](references/AUTHORIZATION_MODEL.md)
   - [Evidence hierarchy](references/EVIDENCE_HIERARCHY.md)
   - [Evidence consolidation](references/EVIDENCE_CONSOLIDATION.md)
   - [Business semantics](references/BUSINESS_SEMANTICS.md)
   - [Dependency reconstruction](references/DEPENDENCY_RECONSTRUCTION.md)
   - [Task modes](references/TASK_MODES.md)
   - [Scope control](references/SCOPE_CONTROL.md)
   - [Protected assets](references/PROTECTED_ASSETS.md)
   - [Frozen capabilities](references/FROZEN_CAPABILITIES.md)
   - [Verification contract](references/VERIFICATION_CONTRACT.md)
   - [Release contract](references/RELEASE_CONTRACT.md)
   - [Delivery closure](references/DELIVERY_CLOSURE.md)

## Authorization boundary

Ordinary implementation requires explicit scoped authorization. General implementation approval does **not** authorize protected actions. When a protected action becomes necessary, set `PROTECTED_ACTION_PENDING`, explain the exact action and impact, and require separate explicit authorization before performing it.

Authorization expires with the approved scope.

## Current truth, history, and conflicts

Resolve conflicts by evidence rank, acceptance status, source lineage, time, then explicit supersession. Recency alone is not authority. A latest explicit accepted decision for the same scope may retire behavior that stale code, screenshots, specs, or tests still contain. Remove retired concepts from current behavior and current regression anchors while preserving immutable historical evidence where traceability requires it.

If evidence still conflicts, mark only the affected scope `UNRESOLVED` and continue independent work.

## Identity and event semantics

Separate canonical identity from historical/source labels. Do not create duplicate entities from aliases without independent evidence. Let transaction evidence determine transaction meaning; settlement evidence does not automatically determine claim/payment type. Define one owner for each economic event so settlement and reporting do not duplicate revenue or cost. Preserve materially different source adjustments as typed facts even when the UI is compact.

## Evidence consolidation

A consolidated index never replaces originals. Preserve provider/source identifiers, lineage, duplicate/version relationships, canonical mappings, and review status. Do not promote “not found here” into “never existed” without checking the relevant primary evidence domains. Exclude credentials, secret stores, agent-state databases, and protected runtime data from convenience consolidation.

## Scope, dependencies, and frozen behavior

Record unrelated discoveries as `OUT_OF_SCOPE_FINDING`; do not silently implement them. A verified capability stays frozen unless evidence demonstrates a correctness conflict; then use `REOPEN_RECOMMENDED`, not automatic modification. When a central module is heavily corrupted, reconstruct from verified surrounding dependency contracts when practical instead of letting the damaged core define upstream/downstream truth.

## Verification and closure

Never claim `PASS`, `VERIFIED`, successful build/migration, or release readiness without direct evidence. Never alter authoritative facts merely to satisfy validation. Releases require cumulative carry-forward regression.

When an explicit delivery-first closure strategy is active, keep release-critical correctness strict but do not let documentation perfection, non-impactful cleanup, repeated audit packaging, or stale superseded verifiers block delivery. Converge on one working candidate and one truthful closure pass.

## Project profiles

Use [PROJECT_PROFILE_TEMPLATE.md](references/PROJECT_PROFILE_TEMPLATE.md) for project-local facts and intentional overrides. Keep real organization/project names, private paths, amounts, and operational history out of the generic skill.
