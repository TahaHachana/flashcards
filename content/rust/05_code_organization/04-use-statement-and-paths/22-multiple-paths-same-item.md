## Multiple Paths to Same Item

Can the same item be accessible through multiple paths? Give an example.

---

**Yes** - through re-exports, the same item can have multiple valid paths.

**Example**:
```rust
// src/lib.rs
pub mod database {
    pub struct Connection {}
}

// Re-export at crate root
pub use database::Connection;

// External users can access via either path:
use my_crate::database::Connection;  // Full path
use my_crate::Connection;             // Re-exported path

// Both refer to the SAME type
```

**Why this is useful**:
- Provide convenient shortcuts
- Maintain backward compatibility
- Offer both detailed and simple paths

**Common in standard library**:
```rust
use std::io::Write;           // Typical path
use std::prelude::v1::Write;  // Also works (via prelude)
```

**Key insight**: Multiple paths can point to the same underlying item through re-exports.

