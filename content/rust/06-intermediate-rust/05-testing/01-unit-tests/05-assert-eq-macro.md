## The assert_eq! Macro

What are the requirements and benefits of using `assert_eq!(left, right)`?

---

Requirements:
- Values must implement `PartialEq` (for comparison)
- Values must implement `Debug` (for error messages)

Benefits over `assert!(left == right)`:
- Shows both actual and expected values on failure
- Clearer failure messages

Example:
```rust
#[test]
fn test_calculation() {
    let result = 2 + 2;
    assert_eq!(result, 4);
}
```

Failure output:
```
assertion `left == right` failed
  left: 5
 right: 4
```

