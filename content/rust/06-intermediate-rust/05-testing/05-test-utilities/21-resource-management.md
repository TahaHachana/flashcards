## Resource Management Pattern

How do you manage test resources (files, connections, etc.) reliably?

---

Use RAII pattern with Drop:

```rust
struct TestResource {
    file_handle: File,
    temp_path: PathBuf,
}

impl TestResource {
    fn new() -> std::io::Result<Self> {
        let temp_path = PathBuf::from("test_file.tmp");
        let file_handle = File::create(&temp_path)?;
        Ok(TestResource { file_handle, temp_path })
    }
    
    fn write(&mut self, data: &[u8]) -> std::io::Result<()> {
        self.file_handle.write_all(data)
    }
}

impl Drop for TestResource {
    fn drop(&mut self) {
        // Cleanup even on panic
        let _ = fs::remove_file(&self.temp_path);
    }
}

#[test]
fn test_resource() -> std::io::Result<()> {
    let mut resource = TestResource::new()?;
    resource.write(b"test data")?;
    // Verify...
    Ok(())
    // Automatic cleanup via Drop
}
```

RAII ensures resources are always cleaned up.

