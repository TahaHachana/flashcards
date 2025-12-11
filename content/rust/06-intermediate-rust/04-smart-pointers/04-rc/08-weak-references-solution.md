## Weak References Solution

What is `Weak<T>`, how does it differ from `Rc<T>`, and how do you use it to prevent reference cycles?

---

`Weak<T>` is a weak reference that doesn't keep data alive - it doesn't contribute to the strong count.

**Key differences:**
- **Strong (`Rc`)**: Keeps data alive, prevents cleanup
- **Weak (`Weak`)**: Doesn't keep data alive, can become invalid

**Creating and using Weak:**
```rust
use std::rc::{Rc, Weak};

// Create weak reference
let rc = Rc::new(String::from("data"));
let weak: Weak<String> = Rc::downgrade(&rc);

println!("Strong: {}", Rc::strong_count(&rc));  // 1
println!("Weak: {}", Rc::weak_count(&rc));      // 1

// Use weak reference (must upgrade)
match weak.upgrade() {
    Some(rc) => println!("Data: {}", rc),  // Data still alive
    None => println!("Data was freed"),     // Data dropped
}
```

**Preventing cycles:**
```rust
struct Node {
    next: Option<Rc<RefCell<Node>>>,      // Strong (child)
    prev: Option<Weak<RefCell<Node>>>,    // Weak (parent)
}

// Child holds strong ref, parent holds weak ref
// No cycle because weak doesn't prevent cleanup
```

**Rule:** Data is freed when strong count reaches 0, regardless of weak count.

