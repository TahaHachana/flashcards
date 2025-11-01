## Binary with Library Pattern

How do you structure a project that has both a library and a binary executable?

---

**Structure**:
```
src/
├── lib.rs           ← Library code (core functionality)
├── main.rs          ← Binary that uses the library
├── database.rs
├── api.rs
└── models/
```

**src/lib.rs**:
```rust
mod database;
mod api;
pub mod models;

pub use database::Database;
pub fn initialize() { /* ... */ }
```

**src/main.rs**:
```rust
use my_app::{Database, initialize};  // Import from library

fn main() {
    initialize();
    let db = Database::new();
    // Application logic
}
```

**Benefits**:
- Library can be tested independently
- Other projects can depend on your library
- Binary is thin, just CLI handling
- Clear separation of concerns

