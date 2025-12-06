## When Deref is Called Automatically

In what two situations does Rust automatically call `deref()`? Provide examples.

---

**1. When using the `*` operator explicitly:**
```rust
let boxed = Box::new(5);
let value = *boxed;  // Calls boxed.deref() then dereferences result
```

**2. When using the dot operator for method calls:**
```rust
use std::ops::Deref;

struct HoldsANumber(u8);

impl Deref for HoldsANumber {
    type Target = u8;
    fn deref(&self) -> &Self::Target { &self.0 }
}

fn main() {
    let my_number = HoldsANumber(20);
    
    // Method from u8, accessed through Deref
    println!("{:?}", my_number.checked_sub(100));
    // Becomes: (*my_number).checked_sub(100)
    // Which is: my_number.deref().checked_sub(100)
}
```

The dot operator automatically dereferences as needed to find the method.

