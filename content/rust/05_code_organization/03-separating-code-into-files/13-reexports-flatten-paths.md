## Re-exports to Flatten Deep Paths

How do you use re-exports to simplify deep module paths?

---

**Problem**: Deep nesting creates long paths
```rust
use my_crate::features::authentication::users::management::CreateUser;
```

**Solution**: Re-export at higher levels
```rust
// src/features/authentication/mod.rs
pub use self::users::management::create::CreateUser;

// Now users can:
use my_crate::features::authentication::CreateUser;
```

**Common pattern in lib.rs**:
```rust
// src/lib.rs
mod database;
mod models;

// Re-export commonly used items at crate root
pub use database::Database;
pub use models::{User, Post};

// Users can now:
use my_crate::{Database, User, Post};
```

**Benefit**: Simpler, more ergonomic API for library users.

