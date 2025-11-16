## Overly Restrictive Bounds Problem

What's the problem with adding unnecessary trait bounds to basic methods?

---

Unnecessary bounds limit which types can use the method:

```rust
// ❌ BAD: new() doesn't need Debug
impl<T: Debug> Wrapper<T> {
    fn new(value: T) -> Self {
        Wrapper { value }
    }
}
// Now only types with Debug can create Wrapper!
```

**Solution**: Only add bounds where actually needed:

```rust
// ✅ GOOD: new() works for any T
impl<T> Wrapper<T> {
    fn new(value: T) -> Self {
        Wrapper { value }
    }
}

// ✅ GOOD: Debug only where needed
impl<T: Debug> Wrapper<T> {
    fn print_debug(&self) {
        println!("{:?}", self.value);
    }
}
```

**Rule**: Minimize bounds to maximize usability.

