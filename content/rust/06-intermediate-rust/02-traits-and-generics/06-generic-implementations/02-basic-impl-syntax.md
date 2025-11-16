## Basic Generic Impl Syntax

What is the correct syntax for implementing methods on a generic struct?

---

Declare the generic parameter after `impl`:

```rust
struct Wrapper<T> {
    value: T,
}

impl<T> Wrapper<T> {
    fn new(value: T) -> Self {
        Wrapper { value }
    }
    
    fn get(&self) -> &T {
        &self.value
    }
}
```

**Critical**: The `<T>` after `impl` is **required**. It declares the generic parameter for the impl block, even though `T` is already declared on the struct.

