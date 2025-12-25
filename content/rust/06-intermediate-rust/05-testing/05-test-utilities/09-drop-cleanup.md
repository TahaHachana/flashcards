## Drop Trait for Cleanup

How can you use the `Drop` trait for automatic test cleanup?

---

Implement `Drop` for automatic cleanup even on panic:

```rust
struct TestGuard {
    db: Database,
}

impl TestGuard {
    fn new() -> Self {
        let mut db = Database::new();
        db.connect();
        db.begin_transaction();
        TestGuard { db }
    }
}

impl Drop for TestGuard {
    fn drop(&mut self) {
        // Automatic cleanup when test ends
        self.db.rollback_transaction();
        self.db.disconnect();
    }
}

#[test]
fn test_with_cleanup() {
    let guard = TestGuard::new();
    
    guard.db.insert_user("Alice");
    assert_eq!(guard.db.count_users(), 1);
    
    // Automatic cleanup on drop (even if test panics!)
}
```

Key benefit: Cleanup happens even if test panics.

RAII (Resource Acquisition Is Initialization) pattern ensures reliability.

