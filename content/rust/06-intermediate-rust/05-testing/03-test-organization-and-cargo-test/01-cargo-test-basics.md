## cargo test Basic Function

What does `cargo test` do when you run it without any arguments?

---

`cargo test` performs these steps:

1. **Discovers** all test functions marked with `#[test]` in:
   - Unit tests (`#[cfg(test)]` modules)
   - Integration tests (`tests/` directory)
   - Doc tests (code in documentation)

2. **Compiles** them in test mode

3. **Runs** tests in parallel by default

4. **Reports** results with summary

Example output:
```
running 5 tests
test test_one ... ok
test test_two ... ok
test test_three ... ok

test result: ok. 5 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out
```

