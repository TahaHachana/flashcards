## Basic Derive Syntax

What is the syntax for deriving multiple traits for a struct?

---

Use `#[derive()]` with a comma-separated list of trait names above the type definition:

```rust
#[derive(Debug, Clone, PartialEq, Eq)]
struct Person {
    name: String,
    age: u32,
}
```

The attribute must be placed directly above the struct/enum definition.

