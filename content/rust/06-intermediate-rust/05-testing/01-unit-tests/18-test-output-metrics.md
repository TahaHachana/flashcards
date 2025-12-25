## Test Result Output Interpretation

What do the different metrics in test output mean?

---

```
test result: ok. 3 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out
```

Metrics:
- **passed**: Tests completed without panicking
- **failed**: Tests that panicked
- **ignored**: Tests marked with `#[ignore]` attribute (not run)
- **measured**: Benchmark tests (performance tests)
- **filtered out**: Tests excluded by command-line filter

Example:
```bash
cargo test addition  # Filters to only tests with "addition"
```

All metrics help you understand test execution scope and results.

