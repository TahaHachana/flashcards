## Smart Pointer Metadata Examples

What metadata does `Vec<T>` store as a smart pointer, and what metadata does `Rc<T>` store?

---

**`Vec<T>` metadata:**
- **Length**: How many elements are currently used
- **Capacity**: How much space is allocated
- **Pointer**: Where the data lives on the heap

**`Rc<T>` metadata:**
- **Strong count**: Number of `Rc` pointers to this data
- **Weak count**: Number of `Weak` pointers to this data

Example:
```rust
let vec = vec![1, 2, 3];
println!("Length: {}", vec.len());
println!("Capacity: {}", vec.capacity());

let rc = Rc::new(5);
println!("Strong count: {}", Rc::strong_count(&rc));
```

