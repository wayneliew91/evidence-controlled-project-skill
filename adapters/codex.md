# Codex Adapter

Use the core `SKILL.md` as the policy entrypoint and keep project-local rules in a separate profile.

## Installation shape

For environments that recognize cross-runtime Agent Skills directories, install this repository as one skill directory, for example under `~/.agents/skills/evidence-controlled-project/`.

## Execution mapping

- Inspect repository instructions, current truth/supersessions, and the active project profile before changing files.
- Local shell, Git, test runners, and patch tools are execution mechanisms, not authorization grants.
- An audit request remains read-only even when the checkout is writable.
- Before implementation, constrain the diff to the explicitly authorized scope and affected dependency boundaries.
- Keep unrelated working-tree changes outside the authorized diff.
- Treat stale tests/verifiers as evidence to classify, not automatically as current truth. Never restore explicitly retired behavior merely to make an obsolete check pass.
- If a central module is corrupted, inspect independently verifiable dependency boundaries before rewriting the core when practical.
- Protected production/runtime/data actions require the separate authorization contract.

## Candidate discipline

During explicit delivery-first closure, converge on one working candidate and compare it with the previous accepted baseline. Do not create extra moving candidates, cleanup branches, or repeated audit packages unless they answer a specific release-critical question.

## Verification

Run task-appropriate checks and retain command/output evidence sufficient to support any `VERIFIED` claim. Release work must apply the cumulative release contract, not only current diff tests. Classify verifier failures as implementation, fixture, superseded-rule, unresolved-evidence, or non-blocking documentation failures before deciding whether they block delivery.
