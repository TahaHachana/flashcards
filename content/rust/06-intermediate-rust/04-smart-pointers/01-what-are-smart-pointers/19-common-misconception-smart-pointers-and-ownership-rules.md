## Common Misconception - Smart Pointers and Ownership Rules

Do smart pointers bypass Rust's ownership rules? Explain the correct understanding.

---

**Misconception:** Smart pointers bypass or circumvent ownership rules.

**Reality:** Smart pointers work *within* ownership rules to enable different ownership *patterns*.

**How they work with ownership:**

1. **`Box<T>`** - Still single ownership, just transfers it:
```rust
let box1 = Box::new(5);
let box2 = box1;  // box1 moved, can't use anymore
```

2. **`Rc<T>`** - Multiple ownership is tracked and enforced:
```rust
let rc1 = Rc::new(5);
let rc2 = Rc::clone(&rc1);  // Explicit clone, count tracked
// Data dropped when count reaches 0
```

3. **`RefCell<T>`** - Enforces borrowing rules at runtime:
```rust
let cell = RefCell::new(5);
let borrow1 = cell.borrow();
let borrow2 = cell.borrow_mut();  // Panics! Already borrowed
```

Smart pointers don't break rules; they provide different ways to satisfy them.

