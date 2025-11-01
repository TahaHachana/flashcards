## Categorized API Pattern

How do you organize re-exports by category, and when is this useful?

---

**Pattern**: Group re-exports into logical modules.

**Implementation**:
```rust
// src/lib.rs
mod internal_db;
mod internal_models;

// Present in logical categories
pub mod db {
    pub use crate::internal_db::connection::Connection;
    pub use crate::internal_db::query::Query;
}

pub mod models {
    pub use crate::internal_models::user::User;
    pub use crate::internal_models::post::Post;
}
```

**Usage**:
```rust
use my_crate::db::{Connection, Query};
use my_crate::models::User;
```

**When useful**:
- Larger libraries with many items
- Clear feature boundaries
- Want to avoid naming conflicts
- Prefer organized namespaces

