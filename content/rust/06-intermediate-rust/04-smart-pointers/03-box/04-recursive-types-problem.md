## Recursive Types Problem

Why can't Rust compile recursive types without `Box`, and what error does the compiler give?

---

Rust needs to know the size of every type at compile time. Recursive types (types that contain themselves) have theoretically infinite size.

**The problem:**
```rust
// ❌ This doesn't compile
struct Node {
    value: i32,
    next: Option<Node>,  // Node contains Node - infinite!
}
```

**Compiler error:**
```
error[E0072]: recursive type `Node` has infinite size
help: insert some indirection (e.g., a `Box`, `Rc`, or `&`)
```

**Why infinite?**
Size of `Node` = size of `i32` + size of `Option<Node>`
But `Option<Node>` contains `Node`, which contains `Option<Node>`, which...
→ Never ends!

**The compiler can't calculate:** "How much memory do I need for this type?"

This is why indirection (like `Box`) is necessary for recursive types.

