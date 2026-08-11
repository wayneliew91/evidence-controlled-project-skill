# Evidence-Controlled Project Skill

A reusable, agent-agnostic governance skill for projects where **evidence authority, change authorization, protected assets, frozen behavior, regression history, and scope control** matter.

It is deliberately organization-neutral. The core repository contains no real company, customer, private path, project amount, credential, or operational history.

## Why this exists

AI agents are often strong at local implementation but can become unreliable when a long-lived project contains conflicting specifications, overwritten behavior, generated derivatives, historical baselines, production data, and prior decisions.

This skill provides a stable control layer so an agent can remain useful without silently changing the definition of truth.

## Core behaviors

- Default to `AUDIT / READ_ONLY`.
- Require explicit scoped authorization for ordinary implementation.
- Require separate second-level authorization for protected actions.
- Resolve conflicting evidence through rank, acceptance, lineage, time, and explicit supersession.
- Mark unresolved evidence `UNRESOLVED` instead of guessing.
- Continue non-blocked work rather than freezing an entire task.
- Record unrelated discoveries as `OUT_OF_SCOPE_FINDING` instead of silently implementing them.
- Keep verified/frozen capabilities closed until explicitly reopened.
- Require direct evidence before claiming `PASS` or `VERIFIED`.
- Require cumulative carry-forward regression for releases.

## Repository structure

```text
.
├── SKILL.md
├── references/
├── adapters/
├── examples/generic-project-profile/
├── tests/
├── scripts/validate_skill.py
└── docs/superpowers/
```

`SKILL.md` is intentionally concise. Detailed rules live in focused references so agents can load only what is relevant.

## Task modes

| Mode | Purpose | Default write posture |
|---|---|---|
| `AUDIT` | Inspect and reconcile evidence | Read-only |
| `DESIGN` | Define accepted behavior/contracts | No implementation by implication |
| `IMPLEMENT` | Apply authorized changes | Scoped writes only |
| `VERIFY` | Prove stated behavior | Read-only unless separately authorized |
| `HANDOFF` | Prepare bounded execution instructions | No authority expansion |
| `RELEASE` | Validate candidate release | Cumulative regression required |

## Authorization model

```text
READ_ONLY
   ↓ explicit scoped implementation approval
IMPLEMENT_AUTHORIZED
   ↓ protected action is required
PROTECTED_ACTION_PENDING
   ↓ separate explicit protected-action approval
PROTECTED_ACTION_AUTHORIZED
```

Finishing the scope returns the agent to `READ_ONLY`.

## Project profiles

The generic skill contains governance, not company rules. Project-specific truth belongs in a profile created from [`references/PROJECT_PROFILE_TEMPLATE.md`](references/PROJECT_PROFILE_TEMPLATE.md).

Profiles use hybrid activation:

- clear project identity → load automatically;
- ambiguous identity → keep generic rules active and do not guess.

A synthetic example is available in [`examples/generic-project-profile/`](examples/generic-project-profile/PROFILE.md).

## Runtime adapters

- [ChatGPT](adapters/chatgpt.md)
- [Codex](adapters/codex.md)
- [Claude](adapters/claude.md)
- [Generic agent](adapters/generic-agent.md)

Adapters map runtime tools to the same core governance; they do not redefine project truth.

## Installation

For runtimes that support Agent Skills directories, clone or copy this repository as one skill directory. A common cross-runtime layout is:

```text
~/.agents/skills/evidence-controlled-project/
```

Some runtimes also support their own local skills directories. See the relevant adapter for integration notes.

For environments without a filesystem skill loader, use `SKILL.md` plus the needed references as project instructions/knowledge, keeping the project profile separate from the generic core.

## Validation

```bash
python3 scripts/validate_skill.py
```

Behavioral pressure scenarios are documented in [`tests/pressure-scenarios.md`](tests/pressure-scenarios.md).

## Design principles

The repository is intentionally distilled:

- no real company/project names;
- no real customers or suppliers;
- no private paths;
- no business amounts;
- no production credentials;
- no dependency on one coding agent;
- no assumption that “newer” means “more authoritative”.

## License

MIT. See [`LICENSE`](LICENSE).
