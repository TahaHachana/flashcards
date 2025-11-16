## Lifetime and Generic Ordering

What is the correct order for lifetimes and generic type parameters in impl blocks?

---

Lifetimes always come before type parameters:

```rust
struct Ref<'a, T> {
    value: &'a T,
}

// ✅ CORRECT: lifetimes first, then types
impl<'a, T> Ref<'a, T> {
    fn new(value: &'a T) -> Self {
        Ref { value }
    }
}

// ❌ WRONG: types before lifetimes
impl<T, 'a> Ref<'a, T> {  // Error!
    // ...
}
```

Pattern: `impl<'lifetime, TypeParam>`

