## Re-exports and Documentation

How do re-exports affect `cargo doc` and documentation?

---

**Effect**: Re-exported items appear in docs at their re-export location.

**Example**:
```rust
mod internal {
    /// A database connection.
    ///
    /// # Examples
    /// ```
    /// let conn = Connection::new();
    /// ```
    pub struct Connection {}
}

/// Re-exported for convenience.
pub use internal::Connection;
```

**In `cargo doc`**:
- `Connection` appears under crate root (where it's re-exported)
- Original documentation is preserved
- Users see the intended API structure

**Best practice**: Document the re-export if you want to add context:
```rust
/// The main connection type.
///
/// This is re-exported from the internal module for convenience.
pub use internal::Connection;
```

**Benefit**: Documentation matches the API users actually use.

