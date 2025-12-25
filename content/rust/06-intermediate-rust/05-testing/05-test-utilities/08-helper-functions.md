## Test Helper Functions Pattern

How do you create and use helper functions in test modules?

---

Helper functions don't have `#[test]` attribute:

```rust
#[cfg(test)]
mod tests {
    use super::*;
    
    // Helper function (not a test)
    fn setup_database() -> Database {
        let mut db = Database::new();
        db.connect();
        db.clear_users();
        db
    }
    
    // Another helper
    fn assert_user_valid(user: &User) {
        assert!(!user.name().is_empty());
        assert!(user.age() > 0);
    }
    
    #[test]
    fn test_user_creation() {
        let db = setup_database();  // Use helper
        let user = create_user("Alice");
        assert_user_valid(&user);   // Use helper
    }
    
    #[test]
    fn test_user_update() {
        let db = setup_database();  // Reuse helper
        let mut user = create_user("Bob");
        user.update_age(26);
        assert_user_valid(&user);
    }
}
```

Benefits: Reduce duplication, consistent setup, reusable assertions.

