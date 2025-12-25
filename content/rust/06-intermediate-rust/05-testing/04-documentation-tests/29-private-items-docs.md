## Doc Test Private Items

Should you write documentation for private items and how do you test them?

---

Yes, document private items for internal clarity:

```rust
/// Public API function.
///
/// # Examples
/// ```
/// let result = process("input");
/// ```
pub fn process(input: &str) -> String {
    validate_and_transform(input)
}

/// Validates and transforms input.
///
/// This is an internal helper function.
/// Used by `process` to ensure input is valid.
///
/// # Examples
/// ```
/// # use my_crate::validate_and_transform;  // Won't work - private!
/// // Can't test private functions in doc tests
/// ```
fn validate_and_transform(input: &str) -> String {
    input.to_uppercase()
}
```

Private item docs:
- Help maintainers understand code
- Not visible in public docs (unless `--document-private-items`)
- Cannot be tested in doc tests
- Use unit tests for private function testing

Document for internal clarity, test with unit tests.

