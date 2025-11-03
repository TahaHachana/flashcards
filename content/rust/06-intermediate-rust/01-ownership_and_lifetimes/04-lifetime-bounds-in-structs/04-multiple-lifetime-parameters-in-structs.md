## Multiple Lifetime Parameters in Structs

When and why would you use multiple lifetime parameters in a struct?
```rust
struct Context<'a, 'b> {
    header: &'a str,
    body: &'b str,
}
```

---

Use multiple lifetime parameters when different fields reference data with independent lifetimes. Here, `header` and `body` can have different lifetimes—the `Context` instance cannot outlive either `'a` or `'b`. This is more flexible than forcing both fields to have the same lifetime, but only use when actually needed (single lifetime is simpler).

