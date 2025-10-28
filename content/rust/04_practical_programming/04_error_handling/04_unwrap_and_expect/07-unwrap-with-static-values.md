## Unwrap With Static Values

When is it safe to use `unwrap()` with compile-time or static values?

---

When parsing static strings or constants you control at compile time:

```rust
use std::net::IpAddr;

// Known at compile time to be valid
const LOCALHOST: IpAddr = "127.0.0.1".parse().unwrap();

lazy_static! {
    static ref REGEX: Regex = Regex::new(r"^\d+$")
        .expect("Regex pattern is valid");
}
```

**Why it's safe:**
- The value is hardcoded and under your control
- If it's invalid, the panic happens at initialization (early)
- You can test it in development
- It won't change based on user input or runtime conditions

Still prefer `expect()` with a message to document the assumption.

