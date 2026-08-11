# Evidence-Controlled Project Skill Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Publish an organization-neutral, agent-agnostic skill that controls evidence use, authorization, scope, protected actions, verification, and release regression.

**Architecture:** Keep `SKILL.md` concise and route detailed governance to focused reference files. Keep runtime-specific behavior in adapters and project-specific constraints in profiles. Validate the repository with a deterministic Python checker and documented pressure scenarios.

**Tech Stack:** Markdown, YAML frontmatter, Python 3 standard library, Git/GitHub.

## Global Constraints

- Default operating posture is `AUDIT / READ_ONLY`.
- Ordinary implementation requires explicit first-level authorization.
- Protected actions require separate second-level authorization.
- Evidence conflicts use rank, acceptance, lineage, time, and supersession; unresolved conflicts remain `UNRESOLVED`.
- Frozen verified capabilities require explicit scoped reopening.
- Out-of-scope discoveries are recorded, not silently implemented.
- Ordinary validation covers scope plus dependencies; releases require cumulative carry-forward regression.
- Public repository content must contain no real organization/project/customer identifiers or private business data.

---

### Task 1: Test contract and validator

**Files:**
- Create: `tests/pressure-scenarios.md`
- Create: `scripts/validate_skill.py`

**Interfaces:**
- Consumes: repository filesystem.
- Produces: exit code `0` only when the required structure, frontmatter, links, key governance terms, and privacy checks pass.

- [x] **Step 1: Define pressure scenarios before writing the skill.**
- [x] **Step 2: Implement repository validator.**
- [x] **Step 3: Run validator before implementation and confirm failure because required production files are absent.**

### Task 2: Core skill and governance references

**Files:**
- Create: `SKILL.md`
- Create: `references/CORE_PRINCIPLES.md`
- Create: `references/AUTHORIZATION_MODEL.md`
- Create: `references/EVIDENCE_HIERARCHY.md`
- Create: `references/TASK_MODES.md`
- Create: `references/SCOPE_CONTROL.md`
- Create: `references/PROTECTED_ASSETS.md`
- Create: `references/FROZEN_CAPABILITIES.md`
- Create: `references/VERIFICATION_CONTRACT.md`
- Create: `references/RELEASE_CONTRACT.md`
- Create: `references/PROJECT_PROFILE_TEMPLATE.md`

**Interfaces:**
- Consumes: approved design specification and pressure scenarios.
- Produces: one concise entrypoint plus focused governance contracts.

- [x] **Step 1: Write minimal `SKILL.md` that triggers and routes correctly.**
- [x] **Step 2: Write focused reference contracts without project-specific data.**
- [x] **Step 3: Run validator and fix structural or privacy failures.**

### Task 3: Runtime adapters and generic project profile

**Files:**
- Create: `adapters/chatgpt.md`
- Create: `adapters/codex.md`
- Create: `adapters/claude.md`
- Create: `adapters/generic-agent.md`
- Create: `examples/generic-project-profile/PROFILE.md`
- Create: `examples/generic-project-profile/BASELINE.md`
- Create: `examples/generic-project-profile/EVIDENCE.md`
- Create: `examples/generic-project-profile/FROZEN_CAPABILITIES.md`
- Create: `examples/generic-project-profile/PROTECTED_ASSETS.md`
- Create: `examples/generic-project-profile/RELEASE_CONTRACT.md`

**Interfaces:**
- Consumes: core governance rules.
- Produces: runtime mapping guidance and a synthetic profile demonstrating the contract.

- [x] **Step 1: Write runtime adapters that do not duplicate business rules.**
- [x] **Step 2: Write synthetic profile with no company identifiers.**
- [x] **Step 3: Run validator.**

### Task 4: Public repository documentation and packaging

**Files:**
- Create: `README.md`
- Create: `LICENSE`
- Create: `.gitignore`
- Create: `tests/README.md`

**Interfaces:**
- Consumes: completed skill repository.
- Produces: public-facing installation/use documentation and an MIT-licensed package.

- [x] **Step 1: Document purpose, installation, modes, authorization, profiles, and adapters.**
- [x] **Step 2: Add MIT license and minimal `.gitignore`.**
- [x] **Step 3: Run full validator and manual content scan.**
- [x] **Step 4: Initialize Git and create a release ZIP.**
- [x] **Step 5: Publish the validated repository to the connected writable GitHub repository.**
