# Evidence Consolidation Contract

## Purpose

Evidence consolidation should make a project easier to reconstruct without destroying provenance. A consolidated index is a navigation and classification layer, not a replacement for authoritative originals.

## Evidence register

For each material artifact, retain enough metadata to trace the conclusion back to its source. Record as applicable:

- source system or location class;
- original file/message/record identifier;
- original artifact name and date;
- party/entity and project mapping status;
- evidence category;
- primary/derived/historical classification;
- canonical identity mapping, if any;
- verification/review status;
- supersession or duplicate relationship;
- notes on conflicts or unresolved fields.

Use hashes when available to distinguish exact duplicates from version conflicts.

## Preserve originals

Do not rewrite original documents to make canonical names, classifications, or totals look cleaner. Canonical mapping belongs in the register or backend mapping layer. Historical artifacts remain evidence of what the source actually said.

Do not treat a summary workbook, migration export, generated report, or copied archive as a substitute for the original when the original remains available.

## Deduplication

Distinguish:

- exact duplicate — same payload/lineage; may be represented once in the active evidence index while preserving archival provenance;
- derived duplicate — transformed/exported copy; keep lineage to its parent;
- version conflict — materially different contents; never collapse without authority;
- repeated archive packaging — same evidence copied into multiple containers; do not count each package as an independent business fact.

## Connected-source collection

When evidence comes from mail, cloud drives, source repositories, chats, or other connectors, preserve the provider-native identifier whenever possible. For an attachment, keep both the parent message/reference and the archived file reference.

## Sensitive exclusions

Do not convenience-copy or ingest secrets and operational agent state merely because they are adjacent to useful evidence. Exclude unless explicitly required and authorized:

- credentials, auth tokens, API keys, passwords;
- secret/config stores;
- local agent state databases, SQLite/WAL files, caches, and telemetry state;
- protected production/runtime data;
- unrelated personal data.

Metadata that a sensitive item exists may be recorded when useful; its contents need not be read.

## Confidence language

Do not promote “not found in the current source” into “never existed in the business.” State the actual scope searched. A negative conclusion becomes strong only after the relevant primary evidence domains have been checked.
