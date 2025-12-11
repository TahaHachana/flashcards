## RefCell Borrowing Rules

What borrowing rules does `RefCell` enforce, and when are they checked?

---

`RefCell` enforces the **same rules as regular Rust**, just at **runtime** instead of compile-time:

1. ✅ **Multiple immutable borrows** - OK
2. ✅ **One mutable borrow** - OK  
3. ❌ **Mutable + immutable together** - Panic!

**Compile-time (regular Rust):**
```rust
let mut x = 5;
let r1 = &x;
let r2 = &x;      // ✅ Multiple immutable OK
// let r3 = &mut x;  // ❌ Won't compile
```

**Runtime (RefCell):**
```rust
use std::cell::RefCell;

let x = RefCell::new(5);
let r1 = x.borrow();
let r2 = x.borrow();      // ✅ Multiple immutable OK
// let r3 = x.borrow_mut();  // ⚠️ Will panic at runtime!
```

**Key difference:**
- Regular Rust: Error at compile time (safer)
- RefCell: Error at runtime (more flexible, can panic)

The rules are identical - only the timing of enforcement changes.

