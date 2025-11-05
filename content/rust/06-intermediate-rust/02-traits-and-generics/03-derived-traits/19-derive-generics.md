## Derive and Generic Types

How do derived traits work with generic types?

---

Derived traits add bounds to the generic parameters. A generic field must implement the derived trait:

```rust
#[derive(Clone)]
struct Wrapper<T> {
    value: T,
}
// Compiler generates:
// impl<T: Clone> Clone for Wrapper<T>

fn main() {
    let w1 = Wrapper { value: 5 };      // ✅ i32 is Clone
    let w2 = w1.clone();
    
    let w3 = Wrapper { value: NoClone };
    // let w4 = w3.clone();  // ❌ Error: NoClone doesn't impl Clone
}
```

The derive automatically adds the necessary trait bounds.

