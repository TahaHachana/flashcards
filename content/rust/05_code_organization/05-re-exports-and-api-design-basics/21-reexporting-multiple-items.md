## Re-exporting Multiple Items Syntax

What are the different ways to re-export multiple items from a module?

---

**Method 1: Individual re-exports**:
```rust
pub use internal::Helper;
pub use internal::Validator;
pub use internal::Parser;
```

**Method 2: Group re-export**:
```rust
pub use internal::{Helper, Validator, Parser};
```

**Method 3: Glob re-export**:
```rust
pub use internal::*;  // Re-export all public items
```

**Method 4: Selective with glob**:
```rust
pub mod utils {
    pub use crate::internal::*;  // All internal utils
}
```

**When to use each**:
- **Individual**: When re-exporting few items with clear intent
- **Group**: When re-exporting several related items
- **Glob**: When re-exporting entire module's contents
- **Selective with glob**: When organizing into categories

**Caution with glob**: Only use when you control the source module.

