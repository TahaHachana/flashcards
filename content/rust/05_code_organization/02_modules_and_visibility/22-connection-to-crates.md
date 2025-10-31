## Connection to Crates and Public APIs

How does visibility in modules relate to a crate's public API?

---

**Connection**: Items marked `pub` in a library crate become part of its public API that other crates can use.

**Within a crate**:
```rust
// src/lib.rs
pub mod parser {
    pub fn parse(input: &str) -> Ast { /* ... */ }
}

mod internal {  // Private - only usable within this crate
    pub fn helper() {}
}
```

**From another crate**:
```rust
use my_crate::parser::parse;  // OK - pub mod, pub fn
// use my_crate::internal::helper;  // ERROR - private module
```

**Key insight**:
- Private items are truly private across crate boundaries
- Public items in a library become your API contract
- Changing public items can break dependent code
- Changing private items is always safe

