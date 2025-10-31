## Modules Are Separate Spaces

Why does this code fail, and how do you fix it?

```rust
use std::fmt::Display;

mod printer {
    pub fn print<T: Display>(item: T) {
        println!("{}", item);
    }
}
```

---

**Problem**: `Display` is not in scope inside the `printer` module. Modules are separate spaces - they don't automatically inherit imports from outer scopes.

**Fix**: Import inside the module:
```rust
mod printer {
    use std::fmt::Display;  // Import in module scope
    
    pub fn print<T: Display>(item: T) {
        println!("{}", item);
    }
}
```

**Key principle**: Each module needs its own `use` statements - imports don't cross module boundaries.

