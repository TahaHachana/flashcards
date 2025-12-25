## Teardown Best Practices

What are best practices for test teardown and cleanup?

---

1. **Prefer automatic cleanup with Drop**:
```rust
impl Drop for TestGuard {
    fn drop(&mut self) {
        self.cleanup();  // Automatic
    }
}
```

2. **Ensure cleanup on panic**:
```rust
// ✅ Good: Drop always runs
struct Guard { resource: Resource }
impl Drop for Guard {
    fn drop(&mut self) {
        self.resource.cleanup();
    }
}

// ❌ Bad: Won't run if test panics
fn manual_cleanup(resource: Resource) {
    resource.cleanup();  // Not called on panic
}
```

3. **Make tests independent**:
```rust
#[test]
fn test_a() {
    let ctx = TestContext::new();  // Fresh state
    // Test...
}  // Cleanup

#[test]
fn test_b() {
    let ctx = TestContext::new();  // Fresh state
    // Test...
}  // Cleanup
```

4. **Use scopes for cleanup timing**:
```rust
#[test]
fn test() {
    {
        let guard = TestGuard::new();
        // Use resource
    }  // Cleanup happens here
    
    // Continue testing with clean state
}
```

Reliable cleanup prevents test pollution.

