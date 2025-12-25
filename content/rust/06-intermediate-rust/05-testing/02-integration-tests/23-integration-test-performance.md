## Integration Test Performance

Why are integration tests typically slower than unit tests, and what's the recommended testing strategy?

---

Integration tests are slower because:
- Each file compiles as separate binary
- Tests exercise more code paths
- May involve more setup/teardown
- Test complete workflows, not isolated functions

Recommended strategy (testing pyramid):
```
        /\
       /  \      Unit Tests (many, fast)
      /____\     - Individual functions
     /      \    - Quick feedback
    /________\   Integration Tests (fewer, slower)
   /          \  - Main workflows
  /____________\ - Verify integration
```

Write:
- Many unit tests for fast feedback
- Fewer integration tests for critical workflows

Balance speed with comprehensive coverage.

