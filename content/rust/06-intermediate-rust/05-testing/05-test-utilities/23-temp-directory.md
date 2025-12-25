## Temporary Directory Pattern

What's the best way to create temporary directories for tests?

---

Use `tempfile` crate or custom implementation:

```rust
use tempfile::TempDir;

#[test]
fn test_with_temp_dir() {
    let temp_dir = TempDir::new().unwrap();
    let file_path = temp_dir.path().join("test.txt");
    
    // Create and test files
    std::fs::write(&file_path, "data").unwrap();
    assert!(file_path.exists());
    
    // Automatic cleanup when temp_dir drops
}
```

Custom implementation:
```rust
struct TestDir {
    path: PathBuf,
}

impl TestDir {
    fn new() -> Self {
        let path = env::temp_dir().join(format!("test_{}", random_id()));
        fs::create_dir(&path).unwrap();
        TestDir { path }
    }
    
    fn path(&self) -> &Path {
        &self.path
    }
}

impl Drop for TestDir {
    fn drop(&mut self) {
        let _ = fs::remove_dir_all(&self.path);
    }
}
```

Temporary directories ensure test isolation.

