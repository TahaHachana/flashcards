## Blanket Implementations in Stdlib

Give an example of a blanket implementation from the standard library and explain how it works.

---

`ToString` is automatically implemented for any type with `Display`:

```rust
// From the standard library:
impl<T: Display> ToString for T {
    fn to_string(&self) -> String {
        // implementation
    }
}

// This means:
struct MyType { value: i32 }

impl Display for MyType {
    fn fmt(&self, f: &mut Formatter) -> Result {
        write!(f, "{}", self.value)
    }
}

fn main() {
    let m = MyType { value: 42 };
    let s = m.to_string();  // Works automatically!
}
```

By implementing `Display`, you automatically get `ToString` for free.

