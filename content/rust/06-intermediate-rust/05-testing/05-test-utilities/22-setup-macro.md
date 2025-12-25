## Setup Macro Pattern

How can you use macros for repetitive test setup?

---

Create setup macros for very repetitive patterns:

```rust
macro_rules! with_database {
    ($db:ident, $code:block) => {
        let mut $db = Database::new();
        $db.connect();
        $db.clear_all();
        $code
    };
}

#[test]
fn test_users() {
    with_database!(db, {
        db.insert_user("Alice");
        assert_eq!(db.count_users(), 1);
    });
}

#[test]
fn test_queries() {
    with_database!(db, {
        db.insert_user("Bob");
        let user = db.find_user("Bob");
        assert!(user.is_some());
    });
}
```

Benefits:
- Very concise
- Consistent setup
- Less boilerplate

Trade-offs:
- Harder to debug
- Less IDE support
- Can hide complexity

Use sparingly - helper functions are usually clearer.

