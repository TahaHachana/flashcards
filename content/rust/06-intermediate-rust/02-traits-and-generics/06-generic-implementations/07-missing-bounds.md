## Missing Trait Bounds Error

What error occurs if you use operations in a generic impl without the required trait bounds?

---

The compiler reports that the operation cannot be applied to the generic type:

```rust
impl<T> Container<T> {
    fn compare(&self, other: &Container<T>) -> bool {
        self.value == other.value
        // ❌ Error: binary operation `==` cannot be applied to type `T`
    }
}
```

**Solution**: Add the necessary trait bound:

```rust
impl<T: PartialEq> Container<T> {
    fn compare(&self, other: &Container<T>) -> bool {
        self.value == other.value  // ✅ Works
    }
}
```

The bound guarantees `T` supports the operation.

