## Combining Test Attributes

How can you combine multiple test attributes like `#[should_panic]` and `#[ignore]`?

---

Stack attributes for combined behavior:

```rust
#[test]
#[ignore]
#[should_panic(expected = "network unavailable")]
fn test_network_failure() {
    // Ignored: can't reliably test
    // Should panic when run with --ignored
    connect_to_invalid_server();
}

#[test]
#[cfg(target_os = "linux")]
#[ignore]
fn test_linux_specific() {
    // Only compiles on Linux
    // Ignored by default
    use_linux_feature();
}
```

With shared setup:
```rust
#[cfg(test)]
mod tests {
    fn setup() -> TestContext {
        TestContext::new()
    }
    
    #[test]
    fn normal_test() {
        let ctx = setup();
        // Normal test
    }
    
    #[test]
    #[should_panic]
    fn panic_test() {
        let ctx = setup();
        // Should panic
    }
    
    #[test]
    #[ignore]
    fn slow_test() {
        let ctx = setup();
        // Slow test
    }
}
```

Attributes are composable for complex scenarios.

