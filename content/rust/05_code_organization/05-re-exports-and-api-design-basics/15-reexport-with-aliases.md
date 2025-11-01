## Re-export with Aliases

How do you change an item's name when re-exporting it?

---

**Use `as` keyword**:
```rust
mod internal {
    pub struct InternalConnectionManager {}
}

// Re-export with simpler name
pub use internal::InternalConnectionManager as Connection;

// Users see the simpler name:
use my_crate::Connection;
```

**When to use**:
- Simplify complex internal names
- Create more user-friendly names
- Avoid naming conflicts
- Match naming conventions at API level

**Example - multiple aliases**:
```rust
pub use database::PgConnection as PostgresConnection;
pub use database::MyConnection as MySQLConnection;
pub use database::SqConnection as SQLiteConnection;
```

**Benefit**: Internal naming for clarity, external naming for usability.

