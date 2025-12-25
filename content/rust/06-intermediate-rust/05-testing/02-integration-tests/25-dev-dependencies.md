## Dev Dependencies for Tests

How can integration tests use additional test-only dependencies?

---

Use `[dev-dependencies]` in Cargo.toml for test-only crates:

**Cargo.toml:**
```toml
[dev-dependencies]
tempfile = "3.8"      # Temporary files for tests
mockito = "1.2"       # HTTP mocking
assert_cmd = "2.0"    # CLI testing
```

**Integration test:**
```rust
// tests/file_operations.rs
use tempfile::tempdir;
use my_project;

#[test]
fn test_file_operations() {
    let dir = tempdir().unwrap();
    let file_path = dir.path().join("test.txt");
    
    my_project::write_file(&file_path, "content").unwrap();
    let content = my_project::read_file(&file_path).unwrap();
    
    assert_eq!(content, "content");
    // dir automatically cleaned up when dropped
}
```

Dev dependencies aren't included in production builds.

