## Rc Purpose and Characteristics

What is `Rc<T>`, when should you use it, and what are its key characteristics?

---

`Rc<T>` (Reference Counted) enables multiple ownership of the same data in single-threaded contexts.

**When to use:**
- When data needs to be shared by multiple parts of your program
- In single-threaded code only
- When data doesn't need mutation (or use with `RefCell` for mutation)

**Key characteristics:**
- Maintains a reference count of owners
- Data is dropped when the last `Rc` is dropped
- Cloning an `Rc` is cheap (only increments counter)
- Use `Rc::clone(&item)` to be explicit about cloning the pointer

Example:
```rust
use std::rc::Rc;
let shared = Rc::new(String::from("data"));
let owner1 = Rc::clone(&shared);  // count = 2
let owner2 = Rc::clone(&shared);  // count = 3
```

