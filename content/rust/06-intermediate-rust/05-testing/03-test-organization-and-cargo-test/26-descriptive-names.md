## Descriptive Test Names Pattern

What naming pattern should you use for test functions and why?

---

Use descriptive names that explain what is tested and expected outcome:

Bad names:
```rust
#[test]
fn test1() { }

#[test]
fn test() { }

#[test]
fn works() { }
```

Good names:
```rust
#[test]
fn parser_rejects_empty_input() { }

#[test]
fn user_age_must_be_positive() { }

#[test]
fn multiply_by_zero_returns_zero() { }

#[test]
fn expired_tokens_are_rejected() { }
```

Pattern: `subject_action_condition` or `expected_behavior_when_condition`

Benefits:
- Self-documenting
- Clear failure messages
- Easy to find relevant tests
- Serves as specification

Example failure:
```
test parser_rejects_empty_input ... FAILED
# Immediately clear what failed
```

