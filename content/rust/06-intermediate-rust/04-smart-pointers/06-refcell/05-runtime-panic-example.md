## Runtime Panic Example

Show code that compiles but panics at runtime with `RefCell`. Why does it compile?

---

```rust
use std::cell::RefCell;

fn main() {
    let cell = RefCell::new(5);
    
    let borrow1 = cell.borrow_mut();  // First mutable borrow
    let borrow2 = cell.borrow_mut();  // ⚠️ Panic!
}
```

**Error at runtime:**
```
thread 'main' panicked at 'already borrowed: BorrowMutError'
```

**Why it compiles:**
- The compiler can't check RefCell borrows at compile time
- RefCell's whole purpose is runtime borrow checking
- The code is syntactically valid

**Why it panics:**
- At runtime, RefCell detects the violation
- Already have one mutable borrow
- Can't have a second one
- Enforces borrowing rules by panicking

**Key insight:** RefCell trades compile-time safety for runtime flexibility. You get more flexibility but must handle potential panics.

