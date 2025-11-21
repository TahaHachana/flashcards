## Closure Recursion Challenge

Can closures be recursive (call themselves)? What makes this difficult?

---

Closures calling themselves is extremely difficult and generally not supported directly.

**Why it's hard:**
```rust
// Doesn't work - closure type not yet known
let factorial = |n| {
    if n == 0 { 1 }
    else { n * factorial(n - 1) } // Can't reference itself
};
```

**Problem:**
- Closure's type is determined by what it captures
- To capture itself, it needs to know its own type
- This creates a circular dependency

**Workaround 1: Use a regular function:**
```rust
fn factorial(n: u32) -> u32 {
    if n == 0 { 1 }
    else { n * factorial(n - 1) }
}
```

**Workaround 2: Use explicit recursion with `Rc` and `RefCell`:**
```rust
use std::rc::Rc;
use std::cell::RefCell;

let factorial = Rc::new(RefCell::new(None));
let f = factorial.clone();

*factorial.borrow_mut() = Some(move |n: u32| -> u32 {
    if n == 0 { 1 }
    else { n * f.borrow().as_ref().unwrap()(n - 1) }
});
```

**Best practice:** For recursion, use regular functions, not closures. Closures are for capturing environment, not complex control flow.

