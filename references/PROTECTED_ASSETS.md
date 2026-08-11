# Protected Assets and Actions

## Protected assets

Treat these as protected unless the active project profile explicitly narrows the category:

- production or live operational data;
- runtime state used by a formal installation;
- release binaries and signed/distributed artifacts;
- credentials, tokens, private keys, secrets, or authentication stores;
- regulated, confidential, personal, financial, or commercially sensitive data;
- historical records whose overwrite would destroy provenance;
- migration targets that cannot be safely reconstructed.

## Protected actions

Require separate second-level authorization for actions such as:

- destructive deletion;
- irreversible migration;
- overwrite of history or production data;
- replacement of formal runtime or release artifacts;
- copying protected data to a new destination;
- exporting credentials or secrets;
- bulk mutation whose rollback is uncertain.

## Before requesting second-level authorization

Document:

1. exact target;
2. operation;
3. necessity;
4. affected scope;
5. expected side effects;
6. backup/recovery/rollback mechanism, if applicable;
7. verification that will prove success or safe failure.

## Backups

Ordinary source/configuration backups may be created non-destructively inside an approved working boundary when useful.

Do not copy protected production/runtime data, credentials, secrets, or sensitive datasets merely for convenience. A backup can itself be a protected data movement.

## External services

Do not upload private project evidence, source, secrets, or sensitive datasets to a new third-party service simply because a tool is convenient. Use only destinations already authorized for that data or obtain the necessary authorization.
