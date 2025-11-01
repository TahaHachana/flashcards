## Prelude Pattern

What is the prelude pattern, and how do you implement it?

---

**Prelude**: A module that re-exports commonly used items for convenient import.

**Implementation**:
```rust
// src/prelude.rs
pub use crate::errors::Error;
pub use crate::results::Result;
pub use crate::traits::{Parse, Validate};

// src/lib.rs
pub mod prelude;
```

**Usage**:
```rust
use my_crate::prelude::*;

// Now have Error, Result, Parse, Validate available
```

**Benefits**:
- One import gets all commonly needed items
- Follows standard library pattern (`use std::prelude::v1::*;`)
- Convenient for library users

**When to use**: When your library has items that users almost always need together.

