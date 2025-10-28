## Unwrap Vs Question Mark

When should you use `?` instead of `unwrap()` or `expect()`?

---

Use `?` when the error should be propagated to the caller:

**Wrong - panics:**
```rust
fn load_config() -> Config {
    let contents = fs::read_to_string("config.toml").unwrap();
    parse_config(&contents).unwrap()
}
```

**Right - propagates errors:**
```rust
fn load_config() -> Result<Config, Error> {
    let contents = fs::read_to_string("config.toml")?;
    parse_config(&contents)
}
```

**General rule:**
- Use `?` for recoverable errors that callers might want to handle
- Use `unwrap()`/`expect()` only when the error truly indicates a bug or when panicking is acceptable (tests, proven invariants)

`?` is almost always the better choice in production code.

