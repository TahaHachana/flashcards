## Generics with Lifetimes

How do you combine generic types with lifetime parameters?

---

Lifetimes come first, then type parameters:

```rust
struct Ref<'a, T> {
    value: &'a T,
}

impl<'a, T> Ref<'a, T> {
    fn new(value: &'a T) -> Self {
        Ref { value }
    }
    
    fn get(&self) -> &'a T {
        self.value
    }
}

fn main() {
    let num = 42;
    let r = Ref::new(&num);
}
```

Pattern: `<'lifetime, TypeParam>` - lifetime parameters before type parameters.

