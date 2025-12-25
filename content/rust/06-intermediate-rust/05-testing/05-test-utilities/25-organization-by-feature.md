## Test Organization by Feature

How should you organize test utility functions and fixtures?

---

Organize by feature area in sub-modules:

```rust
#[cfg(test)]
mod tests {
    use super::*;
    
    mod database_helpers {
        use super::*;
        
        pub fn setup_db() -> Database {
            let mut db = Database::new();
            db.connect();
            db
        }
        
        pub fn assert_user_exists(db: &Database, name: &str) {
            assert!(db.find_user(name).is_some());
        }
    }
    
    mod file_helpers {
        use super::*;
        
        pub fn create_test_file(name: &str) -> TestFile {
            TestFile::new(name)
        }
    }
    
    #[test]
    fn test_user_creation() {
        let db = database_helpers::setup_db();
        create_user(&db, "Alice");
        database_helpers::assert_user_exists(&db, "Alice");
    }
}
```

Benefits: Clear organization, easy to find helpers, grouped by purpose.

