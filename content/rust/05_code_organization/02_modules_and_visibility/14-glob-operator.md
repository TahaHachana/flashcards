## The Glob Operator

What does the glob operator (`*`) do, and when should you use it?

---

**What it does**: Imports all public items from a module.

**Example**:
```rust
mod utilities {
    pub fn read_file() {}
    pub fn write_file() {}
    fn internal_helper() {}  // Private - not imported
}

use utilities::*;  // Import all public items

read_file();       // OK
write_file();      // OK
// internal_helper();  // ERROR - private
```

**When to use**:
- ✅ In tests: `use super::*;`
- ✅ In prelude modules
- ⚠️ Use cautiously in regular code - can make it unclear where items come from

**Better alternative for clarity**:
```rust
use utilities::{read_file, write_file};
```

