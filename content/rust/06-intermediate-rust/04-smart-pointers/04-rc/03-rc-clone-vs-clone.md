## Rc::clone vs .clone()

What's the difference between `Rc::clone(&rc)` and `rc.clone()`, and why is `Rc::clone` preferred?

---

Both work identically, but `Rc::clone(&rc)` is preferred for clarity.

**Example:**
```rust
use std::rc::Rc;

let rc = Rc::new(String::from("data"));

let rc2 = Rc::clone(&rc);  // ✅ Preferred: explicit Rc clone
let rc3 = rc.clone();      // ⚠️  Less clear: might be String clone?
```

**Why `Rc::clone(&rc)` is better:**
- Makes it explicit you're cloning the `Rc` pointer, not the inner data
- Distinguishes from potentially expensive `.clone()` on the inner type
- Conventional in Rust code (signals cheap operation)

**Key insight:** Cloning an `Rc` is cheap (just increments a counter), unlike cloning the data which could be expensive.

**What actually happens:**
```rust
Rc::clone(&rc)  // Increments counter (~2-3 CPU cycles)
rc.clone()      // Same thing, but less obvious it's cheap
```

