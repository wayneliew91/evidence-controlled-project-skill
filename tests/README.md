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

`pressure-scenarios.md` defines discipline tests for:

- authorization and protected actions;
- evidence conflicts and unresolved scope;
- frozen capabilities and scope creep;
- verification and cumulative release regression;
- explicit retirement vs stale specs/tests;
- canonical identity vs historical source labels;
- settlement evidence vs transaction meaning;
- duplicate economic-event prevention;
- typed adjustment preservation;
- traceable evidence consolidation and sensitive exclusions;
- dependency-first reconstruction of a damaged core;
- delivery-first closure and single-candidate convergence;
- avoiding implicit business defaults.

For runtimes with fresh-agent/subagent test support, run each scenario both without the skill (baseline) and with the skill loaded, then compare decisions against the expected behavior. A structural PASS does not substitute for runtime behavioral testing.
