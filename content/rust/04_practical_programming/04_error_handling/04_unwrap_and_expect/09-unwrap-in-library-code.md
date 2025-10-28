## Unwrap In Library Code

Why should library code almost never use `unwrap()` or `expect()`?

---

**Bad - library panics on user error:**
```rust
pub fn parse_user_input(input: &str) -> User {
    let json = serde_json::from_str(input).unwrap();  // Panics!
    User { name: json["name"].as_str().unwrap().to_string() }
}
```

**Good - returns Result:**
```rust
pub fn parse_user_input(input: &str) -> Result<User, ParseError> {
    let json = serde_json::from_str(input)?;
    Ok(User {
        name: json["name"].as_str()
            .ok_or(ParseError::MissingName)?
            .to_string()
    })
}
```

**Reason:** Libraries should let callers decide how to handle errors. Panicking makes the library unusable for applications that need graceful error handling. Always return `Result` in public APIs.

