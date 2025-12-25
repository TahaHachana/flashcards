## Integration Test Naming

What are best practices for naming integration tests?

---

Use descriptive names that explain the workflow being tested:

Bad:
```rust
#[test]
fn test1() { }

#[test]
fn test_function() { }
```

Good:
```rust
#[test]
fn server_handles_concurrent_requests_correctly() { }

#[test]
fn parser_rejects_malformed_json_with_helpful_error() { }

#[test]
fn user_can_complete_full_registration_workflow() { }

#[test]
fn expired_auth_tokens_are_rejected() { }
```

Pattern: `subject_action_condition` or `workflow_description`

Good names serve as documentation of expected behavior.

