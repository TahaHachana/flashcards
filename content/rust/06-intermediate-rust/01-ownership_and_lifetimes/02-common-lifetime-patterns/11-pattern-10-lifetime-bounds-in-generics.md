## Pattern 10 Lifetime Bounds in Generics

When and why do you need the lifetime bound `T: 'a` in generic functions?

```rust
fn store_reference<'a, T>(container: &'a mut Container<T>, item: &'a T)
where
    T: 'a,  // T must live at least as long as 'a
```

---

Use `T: 'a` when a generic type `T` might contain references that need to live at least as long as `'a`. This ensures any references inside `T` remain valid for the duration of `'a`. Common with trait objects and generic containers. Mental shortcut: "Generic might have references inside" → add lifetime bound.

