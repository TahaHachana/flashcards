## Test Naming Best Practices

What are the best practices for naming test functions?

---

Good test names are:

1. **Descriptive**: State what is being tested
2. **Include expected behavior**: Show what should happen
3. **Use snake_case**: Follow Rust conventions
4. **Specific but concise**: Clear without being verbose

Examples:

Bad:
```rust
#[test]
fn test1() { }  // Vague

#[test]
fn test() { }  // Too generic
```

Good:
```rust
#[test]
fn parse_returns_none_for_empty_string() { }

#[test]
fn user_age_must_be_positive() { }

#[test]
fn multiply_by_zero_returns_zero() { }
```

Pattern: `what_happens_when_condition` or `function_behavior_on_input`

