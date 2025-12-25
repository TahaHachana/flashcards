## File System Test Pattern

How do you properly test file system operations with automatic cleanup?

---

Use temporary directory with Drop cleanup:

```rust
use std::fs;
use std::path::PathBuf;

struct TestDirectory {
    path: PathBuf,
}

impl TestDirectory {
    fn new() -> Self {
        let path = PathBuf::from(format!("test_dir_{}", random_id()));
        fs::create_dir(&path).unwrap();
        TestDirectory { path }
    }
    
    fn create_file(&self, name: &str, content: &str) {
        fs::write(self.path.join(name), content).unwrap();
    }
    
    fn path(&self) -> &PathBuf {
        &self.path
    }
}

impl Drop for TestDirectory {
    fn drop(&mut self) {
        // Cleanup: remove directory and contents
        let _ = fs::remove_dir_all(&self.path);
    }
}

#[test]
fn test_files() {
    let dir = TestDirectory::new();
    dir.create_file("test.txt", "Hello");
    
    let content = read_file(&dir.path().join("test.txt"));
    assert_eq!(content, "Hello");
    // Automatic cleanup when dir drops
}
```

