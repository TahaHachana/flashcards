## User-First API Design Principle

What does "user-first thinking" mean in API design, and how do re-exports support it?

---

**User-first thinking**: Design API for how users want to work, not how code is organized internally.

**Anti-pattern** (implementation-first):
```rust
// Organized by implementation concerns
pub mod persistence {
    pub mod relational {
        pub mod postgres { /* Connection here */ }
    }
}

// User must understand implementation:
use my_crate::persistence::relational::postgres::Connection;
```

**User-first** (via re-exports):
```rust
// Internal: organized for maintainability
mod internal_persistence { /* complex structure */ }

// Public: organized for users
pub use internal_persistence::Connection;

// User gets simple import:
use my_crate::Connection;
```

**Principles**:
- Users shouldn't need to know implementation details
- Imports should be intuitive and memorable
- Common cases should be easy

**Re-exports enable**: Separate internal structure from external interface.

