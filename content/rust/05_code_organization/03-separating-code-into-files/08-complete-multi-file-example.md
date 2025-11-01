## Complete Multi-File Example Structure

Show a complete example of a multi-file library structure with proper declarations.

---

**Structure**:
```
my_library/
├── Cargo.toml
└── src/
    ├── lib.rs
    ├── database.rs
    ├── api.rs
    └── models/
        ├── user.rs
        └── post.rs
```

**src/lib.rs**:
```rust
mod database;
mod api;
mod models;

pub use database::Database;
pub use models::{User, Post};
```

**src/models.rs** (modern style):
```rust
pub mod user;
pub mod post;

pub use user::User;
pub use post::Post;
```

**Usage**:
```rust
use my_library::{Database, User, Post};
```

**Note**: `models.rs` declares its submodules and re-exports them for convenience.

