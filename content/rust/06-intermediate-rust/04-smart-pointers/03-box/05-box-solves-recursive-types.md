## Box Solves Recursive Types

How does `Box` solve the recursive type problem? Provide a working example of a linked list node.

---

`Box` provides indirection with a known size (pointer-sized, typically 8 bytes), breaking the infinite size recursion.

**Solution:**
```rust
// ✅ This works!
struct Node {
    value: i32,
    next: Option<Box<Node>>,  // Box has known size
}

fn main() {
    let node3 = Node { value: 3, next: None };
    
    let node2 = Node {
        value: 2,
        next: Some(Box::new(node3)),
    };
    
    let node1 = Node {
        value: 1,
        next: Some(Box::new(node2)),
    };
}
```

**Why this works:**
- `Box<Node>` is always 8 bytes (just a pointer)
- The actual `Node` data is on the heap
- Compiler only needs to know pointer size, not the full recursive structure

**Key insight:** Box has fixed size regardless of what it points to.

