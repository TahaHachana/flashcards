## Progressive Disclosure Pattern

What is progressive disclosure in API design, and how do you implement it with re-exports?

---

**Progressive disclosure**: Make simple things easy, complex things possible.

**Implementation**:
```rust
// src/lib.rs

// Beginner level - at root (easy to find)
pub use database::Connection;
pub use models::User;

// Intermediate level - organized modules
pub mod database {
    pub use crate::internal_db::*;
}

pub mod models {
    pub use crate::internal_models::*;
}

// Advanced level - deeper modules
pub mod advanced {
    pub mod internals {
        pub use crate::internal_db::low_level::*;
    }
}
```

**User experience**:
```rust
// Beginners:
use my_crate::{Connection, User};

// Intermediate:
use my_crate::database::TransactionOptions;

// Advanced:
use my_crate::advanced::internals::RawConnection;
```

**Benefit**: Users discover complexity gradually as they need it.

