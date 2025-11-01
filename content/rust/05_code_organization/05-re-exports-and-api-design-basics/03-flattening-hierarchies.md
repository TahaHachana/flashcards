## Flattening Deep Hierarchies

How do you use re-exports to flatten a deep module hierarchy?

---

**Internal structure** (complex):
```rust
mod database {
    pub mod connection {
        pub struct Connection {}
    }
    pub mod query {
        pub struct Query {}
    }
}
```

**Without re-exports**:
```rust
use my_crate::database::connection::Connection;
use my_crate::database::query::Query;
```

**Flatten with re-exports**:
```rust
// src/lib.rs
pub use database::connection::Connection;
pub use database::query::Query;

// Users write:
use my_crate::{Connection, Query};
```

**Benefit**: Users get a simple API regardless of internal complexity.

