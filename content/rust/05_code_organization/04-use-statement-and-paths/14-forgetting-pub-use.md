## Forgetting Pub Use for Re-exports

What happens if you use `use` instead of `pub use` when trying to re-export items?

---

**Problem**: Items remain private to external users
```rust
// src/lib.rs
mod internal;
use internal::Helper;  // Only visible inside lib.rs!

// External crate:
use my_crate::Helper;  // ERROR: Helper is private
```

**Fix**: Use `pub use` to re-export
```rust
// src/lib.rs
mod internal;
pub use internal::Helper;  // Now external crates can use it

// External crate:
use my_crate::Helper;  // Works!
```

**Key distinction**:
- `use` = bring into current scope (private)
- `pub use` = bring into current scope AND make it public

**Remember**: If you want external users to access something through your crate root, use `pub use`.

