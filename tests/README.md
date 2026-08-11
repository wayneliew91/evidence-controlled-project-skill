# Testing the Skill

## Deterministic validation

Run:

```bash
python3 scripts/validate_skill.py
```

The validator checks:

- required repository structure;
- `SKILL.md` frontmatter and discovery constraints;
- required governance vocabulary;
- relative Markdown links;
- concise `SKILL.md` size;
- known private/project-specific literals that must not enter the public distilled repository.

## Behavioral pressure scenarios

`pressure-scenarios.md` defines discipline tests for authorization, evidence conflicts, scope creep, protected assets, frozen capabilities, verification pressure, and release regression.

For runtimes with fresh-agent/subagent test support, run each scenario both without the skill (baseline) and with the skill loaded, then compare decisions against the expected behavior. A structural PASS does not substitute for runtime behavioral testing.
