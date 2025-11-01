## Breaking Changes from Removing Re-exports

Why is removing a re-export considered a breaking change?

---

**Reason**: Users depend on the re-exported path as part of your public API.

**Example**:
```rust
// Version 1.0
pub use internal::Helper;

// Users write:
use my_crate::Helper;  // This is in their code

// Version 2.0 - you remove the re-export
// pub use internal::Helper;  // Commented out

// Users' code breaks:
use my_crate::Helper;  // ERROR: no longer exists
```

**Solution**: Use deprecation for migration
```rust
// Version 1.5 - deprecate
#[deprecated(since = "1.5.0", note = "Use new::path::Helper instead")]
pub use internal::Helper;

// Version 2.0 - can remove after deprecation period
```

**Rule**: Re-exports are part of your API contract. Removing them requires a major version bump (semver).

