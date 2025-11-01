## Multiple Paths to Same Item

Can the same item be accessible through multiple paths via re-exports?

---

**Yes** - re-exports create additional paths to the same item.

**Example**:
```rust
// src/lib.rs
pub mod database {
    pub struct Connection {}
}

// Re-export at crate root
pub use database::Connection;

// Both paths work and refer to the SAME type:
use my_crate::database::Connection;  // Original path
use my_crate::Connection;             // Re-exported path
```

**Why this is useful**:
- Provide convenient shortcuts
- Maintain backward compatibility (old path + new path)
- Offer detailed and simple paths

**Common in stdlib**:
```rust
use std::io::Write;           // Typical path
use std::prelude::v1::Write;  // Also works (via prelude)
```

**Key insight**: Re-exports create aliases, not copies.

