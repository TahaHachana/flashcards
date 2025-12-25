## Complex Setup Pattern

How do you handle complex test setups with multiple dependencies?

---

Use a comprehensive test fixture:

```rust
struct IntegrationTestContext {
    db: Database,
    server: MockServer,
    temp_dir: TempDir,
    config: Config,
}

impl IntegrationTestContext {
    fn new() -> Self {
        // Setup in correct order
        let temp_dir = TempDir::new().unwrap();
        
        let mut db = Database::new();
        db.connect(&temp_dir.path()).unwrap();
        db.migrate().unwrap();
        
        let config = Config::load(&temp_dir.path()).unwrap();
        
        let server = MockServer::start(8080);
        server.configure(&config);
        
        IntegrationTestContext {
            db,
            server,
            temp_dir,
            config,
        }
    }
    
    fn with_users(mut self, count: usize) -> Self {
        for i in 0..count {
            self.db.create_user(&format!("user{}", i));
        }
        self
    }
}

impl Drop for IntegrationTestContext {
    fn drop(&mut self) {
        // Cleanup in reverse order
        self.server.stop();
        self.db.disconnect();
        // temp_dir drops automatically
    }
}

#[test]
fn test_integration() {
    let ctx = IntegrationTestContext::new()
        .with_users(5);
    // Test with full environment
}
```

