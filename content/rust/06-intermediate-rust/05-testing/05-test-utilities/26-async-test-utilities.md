## Async Test Utilities

How do you create test utilities for async code?

---

Use async test frameworks or manual runtime setup:

With `tokio::test`:
```rust
#[cfg(test)]
mod tests {
    async fn setup_async_context() -> TestContext {
        let db = connect_async().await.unwrap();
        TestContext { db }
    }
    
    #[tokio::test]
    async fn test_async_operation() {
        let ctx = setup_async_context().await;
        let result = async_operation(&ctx.db).await;
        assert!(result.is_ok());
    }
}
```

Manual runtime:
```rust
#[test]
fn test_async() {
    let rt = tokio::runtime::Runtime::new().unwrap();
    rt.block_on(async {
        let ctx = setup_async_context().await;
        // Test async code
    });
}
```

Async cleanup with Drop:
```rust
impl Drop for AsyncTestGuard {
    fn drop(&mut self) {
        // Note: Drop is not async!
        // Use blocking cleanup or spawn task
        tokio::runtime::Handle::current()
            .block_on(async { self.cleanup().await });
    }
}
```

