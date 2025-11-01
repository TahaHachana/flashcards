## Flat Crate Root API Pattern

What is the flat crate root API pattern, and when is it appropriate?

---

**Pattern**: Re-export everything at the crate root for maximum simplicity.

**Implementation**:
```rust
// src/lib.rs
mod database;
mod models;
mod validation;

// Flatten to crate root
pub use database::connection::Connection;
pub use database::query::Query;
pub use models::user::User;
pub use models::post::Post;
pub use validation::email::EmailValidator;
```

**Usage**:
```rust
use my_crate::{Connection, User, EmailValidator};
```

**When appropriate**:
- Small to medium libraries
- Items don't conflict in naming
- Simplicity is the priority

**Caution**: Can become cluttered if you have many items.

