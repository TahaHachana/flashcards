## The Interior Mutability Problem

What problem does interior mutability solve? Show an example where you need to mutate but only have `&self`.

---

**The problem: API requires immutable reference but you need mutation**

```rust
struct PhoneModel {
    company: String,
    model: String,
    on_sale: bool,  // Want to change this
}

impl PhoneModel {
    fn make_not_on_sale(&self) {  // Takes &self, not &mut self
        // ❌ Can't do this!
        // self.on_sale = false;
    }
}
```

**The solution: RefCell**
```rust
use std::cell::RefCell;

struct PhoneModel {
    company: String,
    model: String,
    on_sale: RefCell<bool>,  // Wrapped in RefCell
}

impl PhoneModel {
    fn make_not_on_sale(&self) {
        // ✅ Can mutate through &self!
        *self.on_sale.borrow_mut() = false;
    }
}
```

**Why this matters:**
- API requires `&self` not `&mut self`
- Don't want entire struct mutable
- Need to mutate just one field
- External code expects immutable reference

RefCell allows mutation through an immutable reference by moving borrow checking to runtime.

