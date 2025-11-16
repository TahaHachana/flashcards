## Forgetting Generic Declaration Error

What happens if you forget to declare the generic parameter in an impl block?

---

The compiler treats it as a concrete type and reports it can't be found:

```rust
struct Wrapper<T> {
    value: T,
}

// ❌ WRONG
impl Wrapper<T> {
    fn new(value: T) -> Self {
        Wrapper { value }
    }
}
// Error: cannot find type `T` in this scope
```

**Solution**: Always declare generics after `impl`:

```rust
// ✅ CORRECT
impl<T> Wrapper<T> {
    fn new(value: T) -> Self {
        Wrapper { value }
    }
}
```

