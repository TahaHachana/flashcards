## Feature-Based Organization

How should you organize integration test files?

---

Organize by feature, not by test type:

Good (feature-based):
```
tests/
├── user_authentication.rs
├── data_processing.rs
├── api_endpoints.rs
└── file_operations.rs
```

Bad (type-based):
```
tests/
├── happy_paths.rs
├── error_cases.rs
└── edge_cases.rs
```

Example:
```rust
// tests/user_authentication.rs
use my_project::{User, AuthToken};

#[test]
fn test_successful_login() { }

#[test]
fn test_invalid_credentials() { }

#[test]
fn test_session_expiry() { }
```

Feature-based organization makes tests easier to find and maintain.

