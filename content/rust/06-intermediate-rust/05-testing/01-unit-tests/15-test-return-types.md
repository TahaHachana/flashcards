## Test Return Type Restrictions

What types can test functions return and when would you use each?

---

Test functions can return:

1. **Unit type `()`** (most common):
```rust
#[test]
fn test_basic() {
    assert_eq!(2 + 2, 4);
    // Implicit return of ()
}
```

2. **Result<(), E>** (for error propagation):
```rust
#[test]
fn test_with_result() -> Result<(), Box<dyn Error>> {
    let content = read_file("test.txt")?;
    assert!(content.contains("expected"));
    Ok(())
}
```

Cannot return arbitrary types:
```rust
#[test]
fn invalid() -> i32 {  // Error!
    42
}
```

Use `Result` when testing code that returns `Result` and you want to use `?` operator.

