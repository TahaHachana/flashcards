## Setup and Teardown Pattern

How do you implement setup and teardown for integration tests?

---

Use helper functions for setup and leverage Drop for teardown:

```rust
use my_project::ResourceManager;

fn setup() -> ResourceManager {
    let manager = ResourceManager::new("test_resources");
    manager.initialize().unwrap();
    manager
}

fn teardown(manager: ResourceManager) {
    manager.cleanup().unwrap();
    // Resources cleaned when manager drops
}

#[test]
fn test_resource_management() {
    let manager = setup();
    
    // Test operations
    manager.allocate_resource("test");
    assert!(manager.has_resource("test"));
    
    teardown(manager);
    
    // Verify cleanup
    assert!(!path_exists("test_resources/test"));
}
```

Alternatively, use `Drop` trait for automatic cleanup.

