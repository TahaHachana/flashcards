## The assert_ne! Macro Use Cases

When should you use `assert_ne!(left, right)` instead of `assert_eq!`?

---

Use `assert_ne!` to verify values are NOT equal:

1. **Uniqueness**: IDs or random values must differ
```rust
let id1 = generate_id();
let id2 = generate_id();
assert_ne!(id1, id2, "IDs must be unique");
```

2. **Mutations**: Value changed after operation
```rust
let mut counter = 0;
counter += 1;
assert_ne!(counter, 0);
```

3. **Negative cases**: Shouldn't equal invalid value
```rust
let result = parse("valid");
assert_ne!(result, None);
```

