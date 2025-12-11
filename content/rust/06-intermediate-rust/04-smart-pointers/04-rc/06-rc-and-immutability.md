## Rc and Immutability

Why can't you mutate data through `Rc`, and what's the solution for shared mutable state?

---

**The problem:**
```rust
use std::rc::Rc;

let data = Rc::new(String::from("hello"));

// ❌ Cannot mutate through Rc
// data.push_str(" world");  // Error!
```

**Why?** Multiple owners with mutable access would violate Rust's aliasing rules. `Rc` ensures safety by only allowing shared immutable access.

**The solution: Rc<RefCell<T>>**
```rust
use std::rc::Rc;
use std::cell::RefCell;

let data = Rc::new(RefCell::new(String::from("hello")));
let data2 = Rc::clone(&data);

// Mutate through RefCell (runtime borrow checking)
data.borrow_mut().push_str(" world");

// Both see the change
println!("{}", data.borrow());   // "hello world"
println!("{}", data2.borrow());  // "hello world"
```

**Pattern:** `Rc<RefCell<T>>` is the standard pattern for shared mutable state in single-threaded contexts.

**Trade-off:** Borrow checking moves from compile-time to runtime (can panic).

