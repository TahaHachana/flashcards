## RefCell Purpose and Interior Mutability

What is `RefCell<T>`, what is "interior mutability," and when would you use it?

---

`RefCell<T>` provides interior mutability - the ability to mutate data even when you only have an immutable reference to it.

**How it works:**
- Moves borrow checking from compile time to runtime
- Allows mutation through `&RefCell<T>` (immutable reference)
- Panics at runtime if borrowing rules are violated

**When to use:**
- When you need to mutate data but only have `&T`
- In graph-like data structures where compile-time checking is too restrictive
- Often combined with `Rc`: `Rc<RefCell<T>>` for shared mutable state (single-threaded)

Example:
```rust
use std::cell::RefCell;

let cell = RefCell::new(5);
*cell.borrow_mut() = 10;  // Mutate through immutable reference
println!("{}", cell.borrow());  // 10
```

