## Longest Function Signature Meaning

What does this function signature tell you about lifetime relationships?
```rust
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str
```

---

This signature means:
- There exists some lifetime `'a`
- Both `x` and `y` must be valid for at least `'a`
- The returned reference will be valid for `'a`
- Therefore, the return value is valid as long as BOTH inputs are valid (the shorter of the two lifetimes determines `'a`)

