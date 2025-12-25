## Test Fixtures Pattern

What is the test fixture pattern and how do you implement it?

---

Test fixtures provide reusable test environments:

```rust
struct TestContext {
    db: Database,
    temp_dir: TempDir,
    config: Config,
}

impl TestContext {
    fn new() -> Self {
        let temp_dir = TempDir::new().unwrap();
        let mut db = Database::new();
        db.connect(&temp_dir.path());
        db.initialize_schema();
        
        TestContext {
            db,
            temp_dir,
            config: Config::default(),
        }
    }
    
    fn create_user(&self, name: &str) -> User {
        self.db.insert_user(name)
    }
}

#[test]
fn test_with_fixture() {
    let ctx = TestContext::new();
    let user = ctx.create_user("Alice");
    assert_eq!(ctx.db.count_users(), 1);
    // Auto cleanup when ctx drops
}
```

Benefits: Encapsulates setup, reusable, self-cleaning, consistent environment.

