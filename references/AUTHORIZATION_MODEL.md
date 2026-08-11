# Authorization Model

## States

### `READ_ONLY`

Default state. The agent may inspect, search, compare, classify, reconcile, explain, design, and prepare a plan. It may not modify project artifacts.

### `IMPLEMENT_AUTHORIZED`

Entered only after explicit first-level authorization for a defined scope. Natural language such as “implement the approved changes” is sufficient when the target and scope are clear.

This state permits ordinary edits to source, tests, documentation, and non-protected configuration inside the authorized scope.

### `PROTECTED_ACTION_PENDING`

Use when implementation encounters a protected action. Stop only the protected action, not necessarily the entire task. State:

1. the exact protected asset or operation;
2. why it is needed;
3. expected impact;
4. rollback or recovery path where applicable;
5. what independent work can continue.

### `PROTECTED_ACTION_AUTHORIZED`

Entered only after a second, explicit authorization that clearly covers the protected action. First-level implementation approval cannot be reused as the second authorization.

## Authorization is scope-bound

Approval to modify one component does not authorize:

- unrelated cleanup;
- adjacent feature changes;
- broad renaming;
- historical record correction;
- data migration;
- release replacement;
- protected asset handling.

If scope must expand, record the dependency and obtain explicit expanded authorization.

## Authorization ends

After the authorized task is completed or abandoned, return to `READ_ONLY`. Do not retain standing write permission across later tasks.

## Ambiguous instructions

When an instruction mixes audit and write intent, choose the least destructive interpretation consistent with the request. If the requested write scope is clear, explicit natural-language authorization can be honored. If scope is materially ambiguous, remain read-only for the ambiguous portion.
