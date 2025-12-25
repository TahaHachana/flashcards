## Filtered Out vs Ignored Difference

What's the difference between "filtered out" and "ignored" in test output?

---

They indicate different things:

**Filtered out**: Test exists but doesn't match filter
```bash
$ cargo test addition
test result: ok. 2 passed; 0 failed; 0 ignored; 1 filtered out
              ↑
              test_multiplication didn't match "addition"
```

**Ignored**: Test marked with `#[ignore]`
```rust
#[test]
#[ignore]
fn expensive_test() { }
```

```bash
$ cargo test
test result: ok. 2 passed; 0 failed; 1 ignored; 0 filtered out
              ↑
              expensive_test has #[ignore]
```

Key distinction:
- Filtered out: Excluded by command-line argument
- Ignored: Excluded by `#[ignore]` attribute in code

