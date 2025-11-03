## Elision with Struct Lifetime Parameters

How does elision work with methods on structs that have lifetime parameters?

```rust
struct Container<'a> {
    data: &'a str,
}

impl<'a> Container<'a> {
    fn get_data(&self) -> &str {
        self.data
    }
}
```

---

Rule 3 applies. The returned `&str` is elided to `&'a str` because `self`'s lifetime is `'a`. The explicit version is:
```rust
fn get_data(&self) -> &'a str
```
The method inherits the struct's lifetime parameter for its return type, allowing clean elision in the signature.

