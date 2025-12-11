## Gotcha - Comparing Rc Values vs Pointers

How does `==` work with `Rc`, and how do you compare pointers instead of values?

---

**Comparing values (default):**
```rust
use std::rc::Rc;

let rc1 = Rc::new(String::from("hello"));
let rc2 = Rc::new(String::from("hello"));
let rc3 = Rc::clone(&rc1);

// Compares the inner values, not pointers
assert!(rc1 == rc2);   // ✅ true (both contain "hello")
assert!(rc1 == rc3);   // ✅ true (same value)
```

**Comparing pointers:**
```rust
// Check if Rc's point to same allocation
assert!(!Rc::ptr_eq(&rc1, &rc2));  // ✅ false (different allocations)
assert!(Rc::ptr_eq(&rc1, &rc3));   // ✅ true (same allocation)
```

**When to use each:**
- `==` → Compare values (do they contain the same data?)
- `Rc::ptr_eq()` → Compare pointers (do they point to the same memory?)

**Example use case:**
```rust
// Check if data is actually shared
if Rc::ptr_eq(&rc1, &rc2) {
    println!("Sharing the same data");
} else {
    println!("Different data, even if equal values");
}
```

**Gotcha:** Assuming `==` compares pointers when it actually compares values.

