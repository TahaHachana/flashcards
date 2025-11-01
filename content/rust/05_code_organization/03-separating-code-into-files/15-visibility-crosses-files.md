## Visibility Rules Cross File Boundaries

Do visibility rules (pub, private) work differently when code is split across files?

---

**No** - visibility rules work exactly the same across files.

**Example**:
```rust
// src/database.rs
pub struct Connection {
    url: String,  // Private field, even though in different file
}

impl Connection {
    pub fn new(url: String) -> Self {
        Self { url }
    }
}

// src/lib.rs
mod database;

fn test() {
    let conn = database::Connection::new("localhost".to_string());  // OK
    // let url = conn.url;  // ERROR - field is private
}
```

**Key insight**:
- Files don't create visibility boundaries
- Modules create visibility boundaries
- Whether a module is in one file or split across many doesn't matter
- `pub` and privacy work the same way

