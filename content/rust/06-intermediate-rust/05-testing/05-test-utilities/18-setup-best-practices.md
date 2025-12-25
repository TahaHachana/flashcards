## Setup Function Best Practices

What are best practices for test setup functions?

---

1. **Keep setup functions simple**:
```rust
fn setup_database() -> Database {
    let mut db = Database::new();
    db.connect();
    db.clear_all();
    db
}
```

2. **Return what's needed**:
```rust
fn setup() -> (Database, Config) {
    let db = Database::new();
    let config = Config::default();
    (db, config)
}
```

3. **Make setup infallible** (panic on setup failure):
```rust
fn setup() -> TestContext {
    TestContext::new()
        .unwrap_or_else(|e| panic!("Setup failed: {}", e))
}
```

4. **Use fixtures for complex setup**:
```rust
struct TestFixture {
    db: Database,
    server: MockServer,
    temp_dir: TempDir,
}

impl TestFixture {
    fn new() -> Self { /* ... */ }
}
```

5. **Document requirements**:
```rust
/// Requires: PostgreSQL running on port 5432
fn setup_database() -> Database { /* ... */ }
```

Clear setup makes tests maintainable.

