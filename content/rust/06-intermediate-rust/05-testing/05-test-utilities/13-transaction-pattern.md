## Database Transaction Test Pattern

How do you ensure database test isolation with automatic rollback?

---

Use transaction wrapper with Drop rollback:

```rust
struct TestTransaction<'a> {
    db: &'a mut Database,
}

impl<'a> TestTransaction<'a> {
    fn new(db: &'a mut Database) -> Self {
        db.begin_transaction();
        TestTransaction { db }
    }
}

impl<'a> Drop for TestTransaction<'a> {
    fn drop(&mut self) {
        // Always rollback (even on panic)
        self.db.rollback();
    }
}

#[test]
fn test_isolation() {
    let mut db = Database::new();
    
    {
        let tx = TestTransaction::new(&mut db);
        tx.db.insert_user("Alice");
        assert_eq!(tx.db.count_users(), 1);
    }  // Transaction rolled back here
    
    // Database clean for next test
    assert_eq!(db.count_users(), 0);
}
```

Ensures no test pollution, even with panics.

Each test gets a clean database state.

