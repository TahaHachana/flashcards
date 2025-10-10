## Performance Cost of Heap Operations

Why does Rust make heap operations explicit?

---

Heap operations (allocation, deallocation, cloning) are significantly slower than stack operations. Making them explicit helps developers understand performance costs and encourages efficient stack allocation when possible.

```rust
let x = 5;  // Fast stack
let s = String::from("hello");  // Slower heap allocation
```

