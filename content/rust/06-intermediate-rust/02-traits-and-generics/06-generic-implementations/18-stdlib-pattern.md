## Standard Library Pattern

How does understanding generic implementations help you understand the standard library?

---

Most standard library types use the layered implementation pattern:

```rust
// Vec<T> has methods for all T
impl<T> Vec<T> {
    fn len(&self) -> usize { /* ... */ }
    fn push(&mut self, value: T) { /* ... */ }
}

// Additional methods when T: Clone
impl<T: Clone> Vec<T> {
    fn resize(&mut self, new_len: usize, value: T) { /* ... */ }
}

// Additional methods when T: PartialEq
impl<T: PartialEq> Vec<T> {
    fn contains(&self, x: &T) -> bool { /* ... */ }
}
```

When you see different methods available on `Vec<i32>` vs `Vec<MyType>`, it's because of conditional implementations.

