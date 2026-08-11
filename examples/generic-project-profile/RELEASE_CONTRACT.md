# Release Contract

Before release readiness:

1. Run tests for the changed scope.
2. Run dependency regression for the embedded UI and local data layer.
3. Verify `CAP-EXPORT-001` remains unchanged in behavior.
4. Compare the candidate against the previous accepted baseline for accidental reversion.
5. Record unresolved/deferred items honestly.
6. Verify the produced release artifact directly before claiming release readiness.
