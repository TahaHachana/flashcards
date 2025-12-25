## assert! vs assert_eq! Choice

When should you use `assert!` vs `assert_eq!`?

---

Use `assert_eq!` when comparing concrete values:
```rust
#[test]
fn use_assert_eq() {
    let result = calculate();
    assert_eq!(result, 42);  // Better - shows both values
}
```

Use `assert!` for:

1. Boolean conditions:
```rust
assert!(is_valid);
assert!(count > 0);
```

2. Complex comparisons:
```rust
assert!(result > 0 && result < 100);
```

3. Trait method results:
```rust
assert!(collection.is_empty());
assert!(string.starts_with("prefix"));
```

Why `assert_eq!` is better for equality:
```
// assert_eq! failure:
left: 41
right: 42

// assert! failure:
assertion failed: result == 42
// (doesn't show actual value)
```

