## When to Use Box

List the scenarios when you should use `Box<T>`, and when you should NOT use it.

---

**✅ Use Box when:**

1. **Recursive types:**
```rust
struct Node { next: Option<Box<Node>> }
```

2. **Large data (stack overflow risk):**
```rust
let large = Box::new([0; 1_000_000]);
```

3. **Efficient transfer of large data:**
```rust
fn take(data: Box<LargeStruct>) { }
```

4. **Trait objects (type erasure):**
```rust
fn get() -> Box<dyn Draw> { }
```

5. **Ensure heap allocation:**
```rust
let heap_data = Box::new(value);
```

**❌ Don't use Box when:**

1. **Data is small:** Stack is faster
2. **Need shared ownership:** Use `Rc` or `Arc`
3. **Need interior mutability:** Use `RefCell` or `Mutex`
4. **Performance critical + small data:** Heap allocation overhead matters

**Rule:** Use Box when you specifically need its benefits, not as default.

