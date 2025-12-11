## Gotcha - Storing Ref/RefMut Guards

Why can't you store `Ref` or `RefMut` guards in structs, and what should you do instead?

---

**The problem:**
```rust
use std::cell::{RefCell, Ref};

// ❌ Can't store guards in structs (lifetime issues)
struct Holder<'a> {
    borrow: Ref<'a, Vec<i32>>,  // Won't work well
}
```

**Why it doesn't work:**
- `Ref` and `RefMut` have lifetimes tied to the `RefCell`
- Storing guards creates complex lifetime constraints
- Hard to use the struct without lifetime errors

**Solution: Store RefCell instead**
```rust
// ✅ Store RefCell, not guards
struct Holder {
    cell: RefCell<Vec<i32>>,
}

impl Holder {
    fn get(&self) -> i32 {
        self.cell.borrow()[0]  // Borrow when needed
    }
    
    fn set(&self, value: i32) {
        self.cell.borrow_mut()[0] = value;
    }
}
```

**Pattern:**
- Store `RefCell<T>` in struct
- Create guards (Ref/RefMut) in methods
- Guards live only for method duration
- No lifetime complexity

**Alternative: Use Rc<RefCell<T>>**
```rust
struct Holder {
    data: Rc<RefCell<Vec<i32>>>,
}
```

**Key insight:** Guards are temporary - use them in functions, don't store them.

