## Idiomatic Use Patterns

What are the idiomatic patterns for importing functions vs types in Rust?

---

**For functions**: Import parent module
```rust
use std::fmt;

fn show<T: fmt::Display>(item: T) {
    // Shows it's from fmt module
}
```

**For structs, enums, traits**: Import directly
```rust
use std::collections::HashMap;

let map = HashMap::new();  // Direct access is idiomatic
```

**For items with common names**: Use aliases
```rust
use std::fmt::Result;
use std::io::Result as IoResult;  // Avoid conflict

fn foo() -> Result { /* fmt::Result */ }
fn bar() -> IoResult<()> { /* io::Result */ }
```

**Rationale**: Functions benefit from showing their module; types are unambiguous enough to import directly.

