## Expect Message Best Practices

What makes a good `expect()` message?

---

Good messages explain **why** the operation should succeed:

**Bad messages:**
```rust
value.expect("error");  // Too vague
value.expect("unwrap failed");  // Obvious
value.expect("This should work");  // Not helpful
```

**Good messages:**
```rust
value.expect("Config file must exist at startup");
value.expect("BUG: Vector guaranteed non-empty by precondition");
value.expect("Regex pattern validated at compile time");
value.expect("Database connection established in constructor");
```

**Elements of a good message:**
- Explains the invariant or precondition
- States what went wrong
- May include "BUG:" if this indicates a programming error
- Provides debugging context
- Written for the developer who sees the panic

