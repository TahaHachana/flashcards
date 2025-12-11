## What is RefCell<T>?

What is `RefCell<T>` and what are its key characteristics?

---

`RefCell<T>` provides **interior mutability** - the ability to mutate data even when there are immutable references to it. Unlike normal Rust borrowing which is checked at compile time, `RefCell` enforces borrowing rules at **runtime**.

**Key characteristics:**
- Interior mutability pattern
- Runtime borrow checking (not compile-time)
- Can panic at runtime if rules violated
- Single-threaded only (not thread-safe)
- Allows mutation through immutable reference

**Example:**
```rust
use std::cell::RefCell;

struct Data {
    value: RefCell<i32>,
}

let data = Data {
    value: RefCell::new(5),
};

// Can mutate through immutable reference!
*data.value.borrow_mut() = 10;
```

Think of `RefCell` as saying: "Trust me, I'll follow the borrowing rules, but check them when the program runs instead of when it compiles."

