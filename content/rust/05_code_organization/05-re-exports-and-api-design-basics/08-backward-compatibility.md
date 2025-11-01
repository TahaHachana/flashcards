## Backward Compatibility with Re-exports

How do you use re-exports to maintain backward compatibility when refactoring?

---

**Scenario**: You want to change internal structure but not break users.

**Old structure**:
```rust
pub mod old_location {
    pub struct Connection {}
}
// Users write: use my_crate::old_location::Connection;
```

**New structure with compatibility**:
```rust
// New internal structure
mod new_internal {
    pub struct Connection {}
}

// New, preferred API
pub use new_internal::Connection;

// Keep old path with deprecation
#[deprecated(since = "2.0.0", note = "Use `Connection` at crate root")]
pub mod old_location {
    pub use crate::Connection;
}
```

**Result**: Both old and new code work, with warnings guiding migration.

