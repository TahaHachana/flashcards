## What Does Use Do?

What does the `use` keyword do, and does it make items public?

---

**What `use` does**: Brings items into the current scope for convenient access (creates shortcuts).

**Example**:
```rust
use std::collections::HashMap;

let map = HashMap::new();  // No std::collections:: needed!
```

**Important: `use` does NOT make items public**
```rust
mod my_module {
    use std::collections::HashMap;  // Only visible in my_module
}

// HashMap not available here - it's not public
```

**To make items public**: Use `pub use`
```rust
pub use internal::Helper;  // Now external crates can access Helper
```

**Key point**: `use` is about convenience within a scope, not visibility across scopes.

