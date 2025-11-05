## Cannot Derive for Non-Implementing Fields

What happens if you try to derive a trait when a field doesn't implement it?

---

You get a compiler error. The derive fails because not all fields support the trait.

```rust
struct NoClone;  // Doesn't implement Clone

#[derive(Clone)]  // ❌ Error!
struct Container {
    field: NoClone,
}
// Error: the trait `Clone` is not implemented for `NoClone`
```

**Solution**: Either implement the trait for the field type or don't derive it:
```rust
#[derive(Clone)]
struct NoClone;  // Now implements Clone

#[derive(Clone)]  // ✅ Works!
struct Container {
    field: NoClone,
}
```

