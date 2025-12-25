## Running Single Test Exactly

How do you ensure only one specific test runs, even if multiple tests have similar names?

---

Provide the full test path:

```rust
#[cfg(test)]
mod tests {
    #[test]
    fn test_user() { }
    
    #[test]
    fn test_user_validation() { }
    
    #[test]
    fn test_user_creation() { }
}
```

Problem:
```bash
$ cargo test test_user
# Runs all 3 tests (matches "test_user" substring)
```

Solutions:

1. Use full module path:
```bash
cargo test tests::test_user
# Still might match all three
```

2. Make names unique:
```rust
#[test]
fn user_basic() { }  // Unique name

#[test]
fn user_validation_rules() { }  // Unique name
```

3. Use exact flag (if available in your version):
```bash
cargo test --exact test_user
```

Best practice: Use descriptive, unique test names.

