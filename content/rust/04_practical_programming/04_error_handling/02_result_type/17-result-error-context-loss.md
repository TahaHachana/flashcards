## Result Error Context Loss

Why is it important to preserve error context when converting errors, and how do you do it?

---

Losing error context makes debugging harder:

**Bad - loses information:**
```rust
s.parse().map_err(|_| "Parse error".into())
```

**Better - preserves details:**
```rust
s.parse()
    .map_err(|e| format!("Failed to parse '{}': {}", s, e))
```

Include relevant context (input values, operation being performed) in error messages to aid debugging.

