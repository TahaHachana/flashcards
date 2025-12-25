## Documentation Test Best Practices

What are the best practices for writing documentation tests?

---

1. **Always include examples**:
```rust
/// # Examples
/// ```
/// let result = my_func(42);
/// ```
```

2. **Show common use cases**:
```rust
/// Basic:
/// ```
/// let user = User::new("Alice", 30);
/// ```
///
/// With options:
/// ```
/// let mut user = User::new("Bob", 25);
/// user.set_email("bob@example.com");
/// ```
```

3. **Document error cases**:
```rust
/// ```should_panic
/// divide(10, 0);  // Panics
/// ```
```

4. **Use hidden lines for clarity**:
```rust
/// ```
/// # use my_crate::Config;
/// config.enable_feature("async");
/// ```
```

5. **Keep examples simple**:
- Focus on one thing
- Minimize setup
- Use clear variable names

6. **Use assert_eq! not println!**

Examples should be executable, clear, and trustworthy.

