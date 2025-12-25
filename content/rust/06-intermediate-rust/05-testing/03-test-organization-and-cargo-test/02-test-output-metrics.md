## Test Output Metrics

What do the metrics in test output mean?

---

```
test result: ok. 5 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out
```

Metrics:
- **passed**: Tests completed without panicking
- **failed**: Tests that panicked
- **ignored**: Tests marked with `#[ignore]` (not run)
- **measured**: Benchmark tests (performance tests)
- **filtered out**: Tests excluded by filter argument

Example:
```bash
cargo test addition
# Shows "2 filtered out" if 2 tests don't match "addition"
```

These metrics help understand test execution scope and coverage.

