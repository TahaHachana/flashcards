## Circular Re-export Dependencies

What causes circular re-export dependencies, and how do you fix them?

---

**Problem**: Modules re-exporting each other's items in a cycle.

```rust
// src/lib.rs
pub use a::ItemA;

// src/a.rs
pub use crate::b::ItemB;

// src/b.rs
pub use crate::a::ItemA;  // Circular!
```

**Fixes**:

**1. Extract common module**:
```rust
// src/common.rs
pub struct SharedItem {}

// src/a.rs
pub use crate::common::SharedItem;

// src/b.rs
pub use crate::common::SharedItem;
```

**2. Restructure dependencies**: Usually indicates poor separation of concerns—redesign module boundaries.

**Prevention**: Think carefully about dependency direction when organizing modules.

