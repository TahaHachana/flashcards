## Implementing DerefMut Pattern

What's the pattern for implementing `DerefMut` after you already have `Deref` implemented?

---

**Pattern: Copy Deref, Add Muts**

1. Copy your `Deref` implementation
2. Remove the `type Target` line (inherited from `Deref`)
3. Add `mut` everywhere: `deref_mut`, `&mut self`, `&mut Self::Target`

**Example:**
```rust
use std::ops::{Deref, DerefMut};

struct HoldsANumber(u8);

// Step 1: Implement Deref
impl Deref for HoldsANumber {
    type Target = u8;
    fn deref(&self) -> &Self::Target {
        &self.0
    }
}

// Step 2: Implement DerefMut - copy and add muts
impl DerefMut for HoldsANumber {
    fn deref_mut(&mut self) -> &mut Self::Target {
        &mut self.0
    }
}

fn main() {
    let mut my_number = HoldsANumber(20);
    *my_number = 30;  // Now can mutate through dereference!
}
```

