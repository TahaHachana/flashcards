## Safe Slice Access

How do you safely slice without panicking on invalid indices?

---

Use get() which returns Option instead of panicking.

```rust
let slice = &s[start..end];  // Panics if invalid
let slice = s.get(start..end);  // Returns None if invalid
```

