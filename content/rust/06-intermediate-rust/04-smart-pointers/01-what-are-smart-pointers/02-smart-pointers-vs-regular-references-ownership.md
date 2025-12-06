## Smart Pointers vs Regular References - Ownership

What is the fundamental ownership difference between a regular reference (`&T`) and a smart pointer (like `Box<T>`)?

---

**Regular references (`&T`):**
- Borrow the data without owning it
- When the reference goes out of scope, the data is unaffected
- Cannot outlive the data they reference

**Smart pointers:**
- Own the data they point to
- When the smart pointer goes out of scope, the data is cleaned up automatically
- The data's lifetime is tied to the smart pointer's lifetime

Example:
```rust
let value = 42;
let reference = &value;  // Borrows only

let boxed = Box::new(42);  // Owns the data
```

