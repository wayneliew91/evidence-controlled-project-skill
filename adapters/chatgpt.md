# ChatGPT Adapter

Use the core `SKILL.md` and references as the authoritative governance layer. This adapter contains no project rules.

## Mapping

- Use available conversation files, connected sources, and project context as evidence inputs.
- When a task depends on private project evidence, retrieve that evidence from authorized connected/project sources rather than substituting public web results.
- If multiple connected sources describe the same business event, preserve provider-native IDs and source lineage in the evidence register rather than flattening them into one unattributed summary.
- Treat negative search results narrowly: “not found in this source/search” is not “never existed.”
- Treat tool write capability as separate from authorization. A tool being available does not mean the skill permits using it.
- Keep credentials, secret stores, agent-state databases/caches, and protected runtime data outside convenience evidence collection unless the exact protected action is required and separately authorized.
- If the environment supports persistent project instructions or knowledge files, keep the generic skill separate from the project profile so the skill remains reusable.

## Profile activation

If one profile clearly matches the active project, load it with the generic contract. If profile identity is ambiguous, remain generic and avoid applying project-local constraints until resolved.

When a connected project truth document is older than a later explicit decision in the active conversation/project context, apply the later accepted decision to current behavior and record the supersession; do not rewrite historical evidence.

## Protected writes

Do not turn a first-level implementation request into a protected data/runtime/release write. Follow the authorization states in `references/AUTHORIZATION_MODEL.md`.
