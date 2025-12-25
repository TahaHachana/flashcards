## Test Filtering by Name

How do you run only tests that match a specific name pattern?

---

Provide a filter string after `cargo test`:

```bash
# Run tests with "addition" in the name
cargo test addition
```

Example:
```rust
#[test]
fn test_addition_positive() { }  // Runs

#[test]
fn test_addition_negative() { }  // Runs

#[test]
fn test_multiplication() { }     // Filtered out
```

Output:
```
running 2 tests
test test_addition_positive ... ok
test test_addition_negative ... ok

test result: ok. 2 passed; 0 failed; 0 ignored; 0 measured; 1 filtered out
```

The filter matches any part of the test name or module path.

