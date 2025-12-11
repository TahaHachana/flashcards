## What is Rc<T>?

What is `Rc<T>` and what are its key characteristics?

---

`Rc<T>` (Reference Counted) is a smart pointer that enables **multiple ownership** of the same data in single-threaded contexts. It keeps track of how many references exist to a value and automatically cleans up when the count reaches zero.

**Key characteristics:**
- Enables multiple ownership (multiple `Rc` pointers to same data)
- Single-threaded only (not thread-safe)
- Reference counting overhead (increment/decrement on clone/drop)
- Immutable by default (data cannot be mutated through `Rc` alone)
- Zero owners → automatic cleanup

**Example:**
```rust
use std::rc::Rc;

let data = Rc::new(String::from("shared"));
let data2 = Rc::clone(&data);  // Both own the same data
let data3 = Rc::clone(&data);  // All three share ownership
```

Think of `Rc` as a "shared ownership contract" where data stays alive as long as anyone holds a copy.

