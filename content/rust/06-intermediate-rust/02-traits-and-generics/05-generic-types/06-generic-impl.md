## Implementing Methods on Generic Structs

How do you implement methods for a generic struct?

---

Declare the generic parameter after `impl`:

```rust
struct Wrapper<T> {
    value: T,
}

impl<T> Wrapper<T> {
    fn new(value: T) -> Self {
        Wrapper { value }
    }
    
    fn get(&self) -> &T {
        &self.value
    }
}

fn main() {
    let w = Wrapper::new(42);
    println!("{}", w.get());
}
```

**Critical**: Must write `impl<T>` not just `impl`. The `<T>` declares the generic parameter for use in the impl block.

