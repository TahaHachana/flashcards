## Gotcha Lifetime Bounds with Generics

When do you need the lifetime bound `T: 'a` with generic types in structs?

---

When a generic type `T` might contain references that need to live at least as long as `'a`:
```rust
// Without bound - might not be safe if T has references
impl<'a, T> Container<'a, T> {
    fn new(item: &'a T) -> Self
}

// With bound - ensures T's references live long enough
impl<'a, T: 'a> Container<'a, T> {
    fn new(item: &'a T) -> Self
}
```
The bound ensures any references inside `T` remain valid.

