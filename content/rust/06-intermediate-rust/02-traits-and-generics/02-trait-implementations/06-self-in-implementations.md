## Self in Trait Implementations

What does `Self` mean in a trait implementation, and how can you use it?

---

In trait implementations, `Self` refers to the type you're implementing for.

```rust
trait Factory {
    fn create() -> Self;  // Returns the implementing type
}

impl Factory for Book {
    fn create() -> Self {  // Self means Book here
        Self {
            title: String::from("Untitled"),
            pages: 0,
        }
    }
}
```

You can use `Self` or write the type name explicitly - they mean the same thing.

