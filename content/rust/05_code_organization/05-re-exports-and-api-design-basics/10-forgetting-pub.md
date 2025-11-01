## Forgetting Pub on Re-exports

What happens if you forget `pub` when trying to re-export an item?

---

**Problem**: Item remains private to external users.

```rust
// src/lib.rs
mod internal;
use internal::Helper;  // Missing `pub`!

// External users:
use my_crate::Helper;  // ERROR: Helper is private
```

**Fix**: Add `pub` to the `use` statement:
```rust
// src/lib.rs
mod internal;
pub use internal::Helper;  // Now public!

// External users:
use my_crate::Helper;  // Works!
```

**Key distinction**:
- `use internal::Helper;` = private import (only for current module)
- `pub use internal::Helper;` = public re-export (available externally)

**Remember**: Re-exporting requires `pub use`, not just `use`.

