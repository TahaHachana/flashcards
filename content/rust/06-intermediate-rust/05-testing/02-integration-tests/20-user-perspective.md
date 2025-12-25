## Testing from User Perspective

Why is it important to test from a user's perspective in integration tests?

---

Integration tests should simulate how external users interact with your library:

```rust
// tests/user_workflow.rs
use my_project::{Config, Server};

#[test]
fn test_typical_usage() {
    // How a user would use your library
    
    // 1. Create config
    let config = Config::builder()
        .host("localhost")
        .port(8080)
        .build()
        .unwrap();
    
    // 2. Start server
    let server = Server::new(config);
    
    // 3. Make request
    let response = server.handle_request("/api/users");
    
    // 4. Verify
    assert!(response.is_ok());
}
```

Benefits:
- Ensures public API is sufficient
- Catches usability issues
- Documents intended usage
- Tests realistic workflows

