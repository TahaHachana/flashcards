## Pub Use Basic Syntax

What is the syntax for re-exporting items, and what does it do?

---

**Syntax**:
```rust
pub use path::to::item;
```

**What it does**: Makes an item available at a different path in your module tree, exposing it as part of your public API.

**Example**:
```rust
// src/internal.rs
pub struct Helper {}

// src/lib.rs
mod internal;
pub use internal::Helper;  // Re-export

// Users can now:
use my_crate::Helper;
// Instead of:
use my_crate::internal::Helper;
```

**Key difference**:
- `use` = bring into scope (private)
- `pub use` = bring into scope AND make public

