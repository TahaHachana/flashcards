## Pattern 5 Nested Structs

How do lifetime parameters work with nested structs?

---

The outer struct's lifetime parameter propagates to inner structs. Example:
```rust
struct Name<'a> {
    first: &'a str,
    last: &'a str,
}

struct Person<'a> {
    name: Name<'a>,  // Same lifetime
    age: u32,
}
```
This simplifies to a single lifetime when all references share it. Multiple lifetimes can be used if fields have genuinely different lifetime requirements.

