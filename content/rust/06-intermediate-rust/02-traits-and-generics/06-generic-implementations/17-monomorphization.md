## Connection to Monomorphization

How do generic implementations relate to monomorphization?

---

Each concrete type gets its own specialized implementation at compile time:

```rust
impl<T> Container<T> {
    fn process(&self) {
        // generic implementation
    }
}

fn main() {
    let c1 = Container { value: 5 };
    let c2 = Container { value: "hello" };
}

// Compiler generates specialized versions:
// impl Container<i32> { fn process(&self) { } }
// impl Container<&str> { fn process(&self) { } }
```

This is why generics are zero-cost: at runtime, the code is already specialized with no indirection.

