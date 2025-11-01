## The Prelude Pattern

What is the prelude pattern, and when should you use it?

---

**Prelude**: A module that re-exports commonly used items for convenient import.

**Implementation**:
```rust
// src/prelude.rs
pub use crate::{Error, Result, Connection, User};
pub use crate::traits::{Parse, Validate};

// src/lib.rs
pub mod prelude;
```

**Usage**:
```rust
use my_crate::prelude::*;
// Now have Error, Result, Connection, User, Parse, Validate
```

**When to use**:
- Your library has items almost always needed together
- Want convenience without forcing it
- Following standard pattern (like `std::prelude::v1::*`)

**Benefits**: One import gets all common items, familiar pattern for Rust users.

