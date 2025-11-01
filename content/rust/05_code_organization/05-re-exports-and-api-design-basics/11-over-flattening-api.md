## Over-Flattening the API

What are the problems with over-flattening your API by putting everything at the crate root?

---

**Problem**: Too many items at root creates namespace pollution.

```rust
// src/lib.rs - 50+ re-exports at root
pub use database::Connection;
pub use database::Query;
pub use database::Transaction;
pub use models::User;
pub use models::Post;
pub use models::Comment;
pub use utils::Helper;
pub use utils::Validator;
// ... 40 more items

// Problem: use my_crate::*; imports huge namespace!
```

**Issues**:
- Hard to find specific items
- Naming conflicts more likely
- Overwhelming for users
- Not clear what's important vs advanced

**Better approach**: Use some categorization
```rust
pub use database::Connection;  // Very common at root
pub use models::User;

pub mod db {
    pub use crate::database::*;  // Less common in modules
}
```

**Guideline**: Root for essentials, modules for everything else.

