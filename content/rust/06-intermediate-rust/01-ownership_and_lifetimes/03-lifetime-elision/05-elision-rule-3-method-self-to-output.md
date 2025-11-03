## Elision Rule 3 Method Self to Output

What is Elision Rule 3, and when does it apply?

---

Rule 3: If there are multiple input lifetime parameters, but one is `&self` or `&mut self`, the lifetime of `self` is assigned to all elided output lifetimes.

Example:
```rust
// What you write
impl MyStruct {
    fn get_data(&self) -> &str { ... }
}

// What the compiler sees
impl MyStruct {
    fn get_data<'a>(&'a self) -> &'a str { ... }
}
```

This applies to methods (functions with `self` parameter). Methods typically return references to data owned by `self`—the second most common pattern.

