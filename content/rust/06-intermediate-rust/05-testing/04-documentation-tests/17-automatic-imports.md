## Doc Test Automatic Imports

What imports are automatically available in documentation tests?

---

Doc tests automatically have:

1. **Your crate** (by name from Cargo.toml):
```rust
/// ```
/// // No explicit import needed!
/// let result = my_crate::add(2, 2);
/// ```
```

2. **Standard library prelude**:
```rust
/// ```
/// // Vec, Option, Result, etc. already available
/// let v = Vec::new();
/// let opt = Some(42);
/// ```
```

What you need to import explicitly:
- Other items from your crate
- Standard library items outside prelude
- External dependencies

Example needing imports:
```rust
/// ```
/// # use my_crate::{Config, Parser};  // Need explicit import
/// # use std::collections::HashMap;    // Outside prelude
/// let config = Config::default();
/// ```
```

Your crate name and prelude are automatic, everything else needs importing.

