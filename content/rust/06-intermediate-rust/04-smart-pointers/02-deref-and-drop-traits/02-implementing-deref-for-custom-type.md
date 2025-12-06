## Implementing Deref for Custom Type

Implement `Deref` for a tuple struct `HoldsANumber(u8)` that allows using the `*` operator to access the inner `u8`.

---

```rust
use std::ops::Deref;

struct HoldsANumber(u8);

impl Deref for HoldsANumber {
    type Target = u8;
    
    fn deref(&self) -> &Self::Target {
        &self.0  // Return reference to inner u8
    }
}

fn main() {
    let my_number = HoldsANumber(20);
    println!("{}", *my_number);       // 20
    println!("{}", *my_number + 10);  // 30
}
```

**What happens when you write `*my_number`:**
1. Rust calls `my_number.deref()`
2. Gets back `&u8`
3. Automatically dereferences that `&u8` to get the `u8` value

