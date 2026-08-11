# Claude Adapter

Use the generic skill as reusable governance and keep repository/project instructions as the source of project-local constraints.

## Installation shape

In environments that support local skills, place the skill in the runtime-supported skills directory. Common layouts include `~/.claude/skills/` and the cross-runtime `~/.agents/skills/` alias when supported by the host.

## Execution mapping

- Read project instructions and the unambiguous project profile before acting.
- Do not confuse filesystem access with write authorization.
- Keep audits read-only.
- Apply edits only after explicit scoped implementation authorization.
- Treat destructive, production, runtime, migration, secret, and sensitive-data actions as protected.
- Preserve frozen capabilities unless a scoped reopening is explicitly authorized.

## Handoffs

When delegating work, pass the authorized scope, evidence authority, protected boundaries, frozen capabilities, acceptance criteria, and unresolved items. Delegation does not expand authority.
