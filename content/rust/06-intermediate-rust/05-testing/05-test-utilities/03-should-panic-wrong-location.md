## #[should_panic] Wrong Location Gotcha

What problem occurs when panic happens in unexpected code with `#[should_panic]`?

---

Problem: Test passes if ANY panic occurs, even from wrong location:

```rust
#[test]
#[should_panic]
fn test_divide() {
    let v = vec![];
    let _ = v[0];  // ❌ Panics here (wrong reason!)
    divide(10, 0); // Never reached (intended panic location)
}
```

This test PASSES even though it panics for the wrong reason!

Solution: Use `expected` parameter:

```rust
#[test]
#[should_panic(expected = "divide by zero")]
fn test_divide() {
    let v = vec![];
    let _ = v[0];  // ❌ Fails: panic message doesn't match
}

#[test]
#[should_panic(expected = "divide by zero")]
fn test_divide_correct() {
    divide(10, 0);  // ✅ Passes: correct panic message
}
```

Always use `expected` to verify the correct panic occurs.

