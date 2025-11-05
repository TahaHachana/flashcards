## Deriving vs Manual Implementation

Can you manually implement a trait that could be derived? When would you do this?

---

Yes! Deriving is just automatic implementation. You can always implement manually for custom behavior:

```rust
#[derive(Clone)]  // Auto: clones all fields
struct Auto { value: i32 }

struct Manual { value: i32 }

impl Clone for Manual {
    fn clone(&self) -> Self {
        println!("Custom cloning logic!");
        Manual { value: self.value * 2 }  // Custom behavior
    }
}
```

**When to manual implement**: Custom behavior, optimization, or when derive doesn't exist.

