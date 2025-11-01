## Error and Result Type Pattern

What is the standard pattern for re-exporting Error and Result types in a library?

---

**Pattern**: Define custom Error and Result, re-export at crate root.

**Implementation**:
```rust
// src/error.rs
pub enum Error {
    DatabaseError(String),
    ValidationError(String),
    NotFound,
}

pub type Result<T> = std::result::Result<T, Error>;

// src/lib.rs
mod error;

pub use error::{Error, Result};
```

**Usage**:
```rust
use my_crate::{Result, Error};

fn do_something() -> Result<()> {
    // Uses library's Result type
    Ok(())
}
```

**Benefits**: Convenient for users, less typing, clear association with your library.

