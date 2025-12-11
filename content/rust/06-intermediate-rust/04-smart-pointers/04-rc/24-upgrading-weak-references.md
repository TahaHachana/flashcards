## Upgrading Weak References

How do you safely use a `Weak` reference? What happens if the data was already freed?

---

`Weak` references must be "upgraded" to strong references before use, which can fail if data was dropped.

**Pattern:**
```rust
use std::rc::{Rc, Weak};

fn use_weak(weak: &Weak<String>) {
    match weak.upgrade() {
        Some(rc) => {
            // Data still alive, got strong reference
            println!("Data: {}", rc);
            // rc dropped when scope ends
        }
        None => {
            // Data was freed
            println!("Data no longer available");
        }
    }
}

fn main() {
    let rc = Rc::new(String::from("hello"));
    let weak = Rc::downgrade(&rc);
    
    use_weak(&weak);  // Some("hello")
    
    drop(rc);  // Last strong ref dropped, data freed
    
    use_weak(&weak);  // None (data was freed)
}
```

**Why upgrade can fail:**
- Weak doesn't keep data alive
- If all strong refs dropped, data is freed
- `upgrade()` returns `Option<Rc<T>>`

**Common patterns:**
```rust
// Pattern 1: Early return
if let Some(rc) = weak.upgrade() {
    // Use rc
} else {
    return;  // Data gone
}

// Pattern 2: Conditional logic
let data = weak.upgrade()
    .expect("Data should still be alive");

// Pattern 3: Default value
let data = weak.upgrade()
    .unwrap_or_else(|| Rc::new(default_value()));
```

**Key insight:** Weak is "try to access" not "definitely access".

