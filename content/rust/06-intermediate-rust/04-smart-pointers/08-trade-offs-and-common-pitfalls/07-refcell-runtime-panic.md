## RefCell Runtime Panic

Show code that compiles but panics at runtime with `RefCell`. Why does it compile and why does it panic?

---

```rust
use std::cell::RefCell;

fn main() {
    let cell = RefCell::new(vec![1, 2, 3]);
    
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
- RefCell's purpose is runtime borrow checking
- Code is syntactically valid
- Types are correct

**Why it panics:**
- At runtime, RefCell detects the violation
- Already have one mutable borrow (borrow1)
- Can't have a second mutable borrow
- RefCell enforces rules by panicking

**The borrowing rules (still apply!):**
1. ✅ Multiple immutable borrows
2. ✅ One mutable borrow
3. ❌ Mutable + immutable together

**Trade-off:** RefCell trades compile-time safety for runtime flexibility. You get more flexibility but must handle potential panics.

