## Self Type in Generic Impls

What does `Self` refer to in a generic implementation?

---

`Self` refers to the complete type including all generic parameters:

```rust
struct Wrapper<T> {
    value: T,
}

impl<T> Wrapper<T> {
    fn create_another(value: T) -> Self {
        // Self means Wrapper<T> (the full generic type)
        Wrapper { value }
    }
    
    fn return_self(self) -> Self {
        self  // Returns Wrapper<T>
    }
}
```

Using `Self` is more concise than writing `Wrapper<T>` repeatedly.

