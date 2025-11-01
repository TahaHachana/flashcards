## Hybrid API Approach

What is the hybrid API approach, and what are its benefits?

---

**Pattern**: Common items at root, detailed/advanced items in modules.

**Implementation**:
```rust
// src/lib.rs
mod database;
mod models;

// Common items at root (convenience)
pub use database::Connection;
pub use models::User;

// Detailed items in namespaces (organization)
pub mod db {
    pub use crate::database::*;
}

pub mod advanced {
    pub use crate::database::internal::*;
}
```

**Usage**:
```rust
// Most users write:
use my_crate::{Connection, User};

// Power users can access:
use my_crate::db::TransactionOptions;
use my_crate::advanced::InternalAPI;
```

**Benefits**: Balance between simplicity and completeness, progressive disclosure.

