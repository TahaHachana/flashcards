## Box Purpose and Use Cases

What is `Box<T>` and what are its three main use cases?

---

`Box<T>` is a smart pointer that allocates data on the heap instead of the stack.

**Three main use cases:**

1. **Recursive types** - Types that contain themselves:
```rust
struct Node {
    value: i32,
    next: Option<Box<Node>>,  // Box has known size
}
```

2. **Large data** - Avoid stack overflow with large allocations:
```rust
let large = Box::new([0; 1_000_000]);
```

3. **Trait objects** - Type erasure with dynamic dispatch:
```rust
let animal: Box<dyn Animal> = Box::new(Dog);
```

