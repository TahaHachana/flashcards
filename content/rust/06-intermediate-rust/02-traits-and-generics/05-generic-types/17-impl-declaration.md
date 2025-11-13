## Generic Impl Block Declaration

What's wrong with this code, and how do you fix it?

```rust
struct Wrapper<T> {
    value: T,
}

impl Wrapper<T> {
    fn new(value: T) -> Self {
        Wrapper { value }
    }
}
```

---

**Problem**: `T` is not declared in the impl block.

**Solution**: Declare `<T>` after `impl`:

```rust
impl<T> Wrapper<T> {
    fn new(value: T) -> Self {
        Wrapper { value }
    }
}
```

The generic parameter must be declared for the impl block to use it, even though it's already declared on the struct.

