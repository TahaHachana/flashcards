## Two-Layer Approach

What is the two-layer approach to API design, and why is it important?

---

**Two layers**:

**Internal layer** (implementation):
```rust
// Organize for maintainability
mod internal_database;
mod internal_models;
mod internal_validation;
```

**Public layer** (API):
```rust
// Organize for usability
pub use internal_database::Connection;
pub use internal_models::User;
pub use internal_validation::EmailValidator;
```

**Why important**:
- **Separation of concerns**: Internal structure ≠ API structure
- **Flexibility**: Change internals without breaking API
- **Optimization**: Each layer optimized for different goals
- **Maintainability**: Clear distinction between private and public

**Key principle**: Internal organization optimizes for code maintainability. Public API optimizes for user experience. Re-exports bridge the two.

