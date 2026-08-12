# Dependency Reconstruction

## Use dependency evidence before rewriting a damaged core

A central module can become the least reliable place to learn its own intended behavior after repeated rewrites, migrations, or partial regressions. When surrounding modules independently produce authoritative inputs or outputs to that core, use those boundaries to reconstruct truth before redesigning the center.

## Dependency-first sequence

1. Identify the damaged or disputed core.
2. Map its inbound and outbound dependency surfaces.
3. Classify which surrounding modules hold primary facts, derived outputs, or merely cached copies.
4. Audit independent evidence-producing modules first when they can progress safely.
5. Freeze verified dependency contracts.
6. Reconstruct the core from accepted business truth plus those dependency contracts.
7. Run cross-boundary regression after the core is repaired.

This is an ordering heuristic, not a universal rule. If the core blocks access to all usable evidence or prevents independent verification, document that constraint and adapt the order.

## Do not let corrupted structure define truth

Avoid these failure modes:

- using current navigation/layout as proof of intended business boundaries;
- using current database grouping as proof of canonical identity;
- inferring upstream business rules from a downstream report that may itself be stale;
- redesigning a verified mapping/integration merely because the core was rewritten;
- rebuilding every dependency at once instead of isolating the damaged surface.

## Frozen integration boundaries

If a mapping, link, export, or other integration has already been independently verified, treat it as a frozen contract while reconstructing nearby modules. Verify that later changes do not break it; do not reopen it without evidence of a correctness conflict.

## Reconstruction matrix

For a complex core, build a matrix such as:

```text
canonical entity/event
-> source authority
-> inbound facts
-> derived calculations
-> settlement/state changes
-> outbound reports/exports
-> historical aliases/snapshots
-> unresolved conflicts
```

This keeps source facts, calculations, and presentation from being accidentally merged into one layer.
