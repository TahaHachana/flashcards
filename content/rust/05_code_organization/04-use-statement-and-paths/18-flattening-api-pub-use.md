## Flattening API with Pub Use

How do you use `pub use` to create a clean, flat API for your library?

---

**Internal organization** (complex structure):
```rust
// src/lib.rs
mod database {
    pub mod connection {
        pub struct Connection {}
    }
}

mod models {
    pub mod user {
        pub struct User {}
    }
}
```

**Flatten with `pub use`**:
```rust
// src/lib.rs
mod database;
mod models;

// Re-export at crate root
pub use database::connection::Connection;
pub use models::user::User;
```

**User experience**:
```rust
// Without pub use:
use my_crate::database::connection::Connection;
use my_crate::models::user::User;

// With pub use (much cleaner!):
use my_crate::{Connection, User};
```

**Benefit**: Hide internal complexity, present simple API.

