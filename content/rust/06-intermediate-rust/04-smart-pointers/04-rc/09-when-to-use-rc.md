## When to Use Rc

List four scenarios when you should use `Rc<T>` and four when you shouldn't.

---

**✅ Use Rc when:**

1. **Multiple parts need to own the same data:**
```rust
struct Graph {
    nodes: Vec<Rc<Node>>,
}
```

2. **Avoid expensive clones:**
```rust
let expensive = Rc::new(large_string);  // Share cheaply
```

3. **Avoid complex lifetime annotations:**
```rust
struct City {
    name: Rc<String>,  // No lifetime needed
}
```

4. **Building tree/graph structures:**
```rust
struct Node {
    children: Vec<Rc<Node>>,
    parent: Weak<Node>,
}
```

**❌ Don't use Rc when:**

1. **Single ownership suffices:**
```rust
let data = String::from("hello");  // Better than Rc
```

2. **Need thread safety:**
```rust
// Use Arc instead for multi-threaded
```

3. **Need mutability:**
```rust
// Use Rc<RefCell<T>> for interior mutability
```

4. **Performance is critical:**
```rust
// Rc has overhead; stack allocation is faster
```

