## Confusing Re-export Locations

What makes a re-export location confusing, and how do you avoid it?

---

**Problem**: Re-exporting items in illogical locations.

**Confusing**:
```rust
pub mod models {
    // Why is Connection in models module?
    pub use crate::database::Connection;  
}

// Users confused:
use my_crate::models::Connection;  // Doesn't make sense!
```

**Better**:
```rust
pub mod database {
    pub use crate::internal_db::Connection;
}

// Or at crate root:
pub use internal_db::Connection;

// Now it makes sense:
use my_crate::database::Connection;
use my_crate::Connection;
```

**Guidelines**:
- Re-export in logical locations (by functionality)
- Match user expectations
- Group related items together
- Use clear module names

**Mental model**: Ask "where would users naturally look for this?"

