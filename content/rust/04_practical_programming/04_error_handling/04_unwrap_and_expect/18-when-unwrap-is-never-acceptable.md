## When Unwrap Is Never Acceptable

In what situations should you **never** use `unwrap()` or `expect()`?

---

**Never use in:**

1. **Public library APIs** - Let callers handle errors
```rust
pub fn parse(input: &str) -> Result<Data, Error>  // Good
pub fn parse(input: &str) -> Data  // Bad if it can unwrap
```

2. **User input handling** - Users control the input
```rust
// Never unwrap user-provided data
user_input.parse().unwrap()  // ❌
```

3. **Network/IO operations** - These can always fail
```rust
// Network is unreliable
http_request().unwrap()  // ❌
```

4. **File operations** - Files may not exist, be locked, etc.
```rust
// Unless it's a test resource
File::open(user_path).unwrap()  // ❌
```

5. **Production servers** - Crashes affect users
```rust
// In web handlers, background jobs, etc.
db_query().unwrap()  // ❌
```

**Rule:** If users, network, or external systems are involved, handle errors properly.

