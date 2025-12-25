## When to Use --nocapture

When should you use `--nocapture` in testing?

---

Use `--nocapture` when:

1. **Debugging failing tests**:
```rust
#[test]
fn debug_test() {
    println!("Step 1: Initialize");
    let data = initialize();
    println!("Step 2: Process - data length: {}", data.len());
    let result = process(data);  // Fails here
    println!("Step 3: Verify");  // Never reached
}
```

2. **Verifying print statements work**:
```rust
#[test]
fn test_logging() {
    println!("Testing logger...");
    log_message("test");
}
```

3. **Understanding test execution flow**:
```rust
#[test]
fn complex_test() {
    println!("Starting");
    for i in 1..=5 {
        println!("Iteration {}", i);
    }
}
```

Run with: `cargo test -- --nocapture`

