## Type Conversion Pattern

How can you implement a method that converts a generic type to another generic type?

---

Use a method with a new generic parameter and a closure:

```rust
struct Wrapper<T>(T);

impl<T> Wrapper<T> {
    fn map<U, F>(self, f: F) -> Wrapper<U>
    where
        F: FnOnce(T) -> U,
    {
        Wrapper(f(self.0))
    }
}

fn main() {
    let w = Wrapper(5);
    let w2 = w.map(|x| x.to_string());
    // Wrapper<i32> → Wrapper<String>
}
```

This pattern allows transforming the wrapped value's type.

