## Gotcha Elision in Struct Methods

What lifetime does the return value have in this method?
```rust
struct Holder<'a> {
    value: &'a str,
}

impl<'a> Holder<'a> {
    fn get(&self) -> &str {
        self.value
    }
}
```

---

Due to elision Rule 3, `&str` expands to `&'a str` (the struct's lifetime parameter), not a lifetime tied to the `&self` borrow. Explicit version:
```rust
fn get(&self) -> &'a str { self.value }
```
This returns a reference with the struct's lifetime, which makes sense since it's returning the struct's stored data.

