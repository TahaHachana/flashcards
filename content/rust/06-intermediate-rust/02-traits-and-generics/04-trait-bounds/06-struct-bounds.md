## Trait Bounds on Structs

How do you add trait bounds when defining a generic struct?

---

Add bounds directly on the type parameter in the struct definition:

```rust
struct Container<T: Clone> {
    value: T,
}

impl<T: Clone> Container<T> {
    fn new(value: T) -> Self {
        Container { value }
    }
    
    fn duplicate(&self) -> T {
        self.value.clone()  // Can use .clone() because of bound
    }
}
```

The bound applies to all uses of the type parameter.

