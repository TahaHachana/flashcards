## RefCell vs Cell for Copy Types

When should you use `Cell` instead of `RefCell` for interior mutability? What's the difference?

---

**Cell: For `Copy` types only**
```rust
use std::cell::Cell;

let cell = Cell::new(5);

// Simple get/set, no borrowing
let value = cell.get();  // Gets copy
cell.set(10);            // Sets value
```

**RefCell: For any type**
```rust
use std::cell::RefCell;

let refcell = RefCell::new(vec![1, 2, 3]);

// Need to borrow
let value = refcell.borrow();  // Returns guard
refcell.borrow_mut().push(4);  // Mutable guard
```

**Comparison:**

| Feature | Cell | RefCell |
|---------|------|---------|
| **Works with** | Copy types only | Any type |
| **Borrow checking** | None | Runtime |
| **Methods** | `get()`, `set()` | `borrow()`, `borrow_mut()` |
| **Can panic** | No | Yes |
| **Overhead** | Zero | Small |

**When to use Cell:**
```rust
struct Config {
    enabled: Cell<bool>,      // ✅ bool is Copy
    count: Cell<u32>,         // ✅ u32 is Copy
    // name: Cell<String>,    // ❌ String is not Copy
}

// Simple to use
config.enabled.set(true);
let is_enabled = config.enabled.get();
```

**When to use RefCell:**
```rust
struct Config {
    name: RefCell<String>,      // String not Copy
    items: RefCell<Vec<Item>>,  // Vec not Copy
}

// Need borrowing
*config.name.borrow_mut() = "new".to_string();
```

**Rule:** If type is `Copy`, prefer `Cell` (simpler, no panics). Otherwise use `RefCell`.

