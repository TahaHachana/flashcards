## Testing Public API End-to-End

What is the recommended pattern for testing complete workflows in integration tests?

---

Test complete workflows, not individual functions:

```rust
// tests/workflow_test.rs
use my_project::{Database, Query};

#[test]
fn test_full_database_workflow() {
    // Setup
    let mut db = Database::new();
    
    // Insert
    let id = db.insert("Alice", 30).unwrap();
    
    // Query
    let result = db.query(Query::ByName("Alice"));
    assert!(result.is_ok());
    assert_eq!(result.unwrap().len(), 1);
    
    // Update
    db.update(id, "age", "31").unwrap();
    
    // Verify
    let user = db.get(id).unwrap();
    assert_eq!(user.age(), 31);
}
```

This tests that modules integrate correctly through the public API.

