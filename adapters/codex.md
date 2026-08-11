# Codex Adapter

Use the core `SKILL.md` as the policy entrypoint and keep project-local rules in a separate profile.

## Installation shape

For environments that recognize cross-runtime Agent Skills directories, install this repository as one skill directory, for example under `~/.agents/skills/evidence-controlled-project/`.

## Execution mapping

- Inspect repository instructions and the active project profile before changing files.
- Local shell, Git, test runners, and patch tools are execution mechanisms, not authorization grants.
- An audit request remains read-only even when the checkout is writable.
- Before implementation, state or infer only the explicitly authorized scope.
- Keep unrelated working-tree changes outside the authorized diff.
- Protected production/runtime/data actions require the separate authorization contract.

## Verification

Run task-appropriate checks and retain command/output evidence sufficient to support any `VERIFIED` claim. Release work must apply the cumulative release contract, not only current diff tests.
