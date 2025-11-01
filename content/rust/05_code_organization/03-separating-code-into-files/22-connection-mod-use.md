## Connection Between Mod and Use

How do `mod` declarations and `use` statements work together when organizing multi-file projects?

---

**Two-step process**:

**Step 1 - Declare modules** (`mod`):
```rust
// src/lib.rs
mod database;  // Makes module exist
mod api;
```

**Step 2 - Import items** (`use`):
```rust
// src/lib.rs
use database::Connection;  // Import specific items
use api::Router;
```

**Common pattern - Re-export**:
```rust
// src/lib.rs
mod database;      // Declare (private by default)
mod api;

pub use database::Connection;  // Re-export publicly
pub use api::Router;

// Users of your crate can now:
// use my_crate::{Connection, Router};
```

**Remember**: `mod` makes it exist, `use` makes it convenient, `pub use` makes it available to others.

