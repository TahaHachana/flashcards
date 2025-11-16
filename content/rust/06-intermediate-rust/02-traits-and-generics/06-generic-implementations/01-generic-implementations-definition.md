## What Are Generic Implementations?

What are generic implementations and why do they matter?

---

Generic implementations are impl blocks that provide methods for generic types. They allow you to write methods once that work for any type `T`, or only for types that meet certain requirements.

```rust
struct Container<T> {
    value: T,
}

// Methods for ALL types T
impl<T> Container<T> {
    fn new(value: T) -> Self {
        Container { value }
    }
}

// Methods only when T implements Display
impl<T: Display> Container<T> {
    fn print(&self) {
        println!("{}", self.value);
    }
}
```

**Why they matter**: Write once, use everywhere; provide conditional functionality; create flexible APIs.

