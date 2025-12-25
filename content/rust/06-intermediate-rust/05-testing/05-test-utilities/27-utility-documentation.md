## Test Utility Documentation

How should you document test utilities and helper functions?

---

Document test utilities clearly:

```rust
#[cfg(test)]
mod test_helpers {
    use super::*;
    
    /// Creates a test database with clean state.
    ///
    /// The database is automatically cleaned up when dropped.
    ///
    /// # Panics
    ///
    /// Panics if database connection fails.
    pub fn setup_test_db() -> TestDatabase {
        TestDatabase::new()
            .expect("Failed to setup test database")
    }
    
    /// Asserts that a user with the given name exists.
    ///
    /// # Panics
    ///
    /// Panics if user is not found or database query fails.
    pub fn assert_user_exists(db: &Database, name: &str) {
        let user = db.find_user(name)
            .expect("Database query failed");
        assert!(user.is_some(), "User '{}' not found", name);
    }
    
    /// Builder for creating test users with custom properties.
    pub struct TestUserBuilder {
        // ...
    }
}
```

Good documentation helps other developers use test utilities correctly.

