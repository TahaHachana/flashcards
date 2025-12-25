## Running Integration Tests Commands

What commands can you use to run integration tests?

---

```bash
# Run all tests (unit + integration)
cargo test

# Run only integration tests
cargo test --test '*'

# Run specific integration test file
cargo test --test integration_test

# Run specific test within a file
cargo test --test integration_test test_name

# Show output for passing tests
cargo test -- --nocapture

# Run single-threaded (for debugging)
cargo test -- --test-threads=1
```

Example output:
```
running 2 tests (src/lib.rs unit tests)
test tests::unit_test ... ok

running 3 tests (integration_test)
test test_api ... ok
test test_workflow ... ok
```

Integration tests show their filename in output.

