## String Literals Are Slices

What type are string literals?

---

&str. They're slices pointing to specific points in the binary, which is why they're immutable.

```rust
let s: &str = "Hello, world!";
```

