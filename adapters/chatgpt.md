# ChatGPT Adapter

Use the core `SKILL.md` and references as the authoritative governance layer. This adapter contains no project rules.

## Mapping

- Use available conversation files, connected sources, and project context as evidence inputs.
- When a task depends on private project evidence, retrieve that evidence from authorized connected/project sources rather than substituting public web results.
- Treat tool write capability as separate from authorization. A tool being available does not mean the skill permits using it.
- If the environment supports persistent project instructions or knowledge files, keep the generic skill separate from the project profile so the skill remains reusable.

## Profile activation

If one profile clearly matches the active project, load it with the generic contract. If profile identity is ambiguous, remain generic and avoid applying project-local constraints until resolved.

## Protected writes

Do not turn a first-level implementation request into a protected data/runtime/release write. Follow the authorization states in `references/AUTHORIZATION_MODEL.md`.
