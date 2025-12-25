## Module Visibility Gotcha

What common mistake occurs with module visibility in integration tests?

---

Problem: Making function public but forgetting the module:

```rust
// src/lib.rs
pub mod parser {  // Module is public
    fn parse(input: &str) -> String {  // Function NOT public
        input.to_uppercase()
    }
}
```

```rust
// tests/test.rs
#[test]
fn broken() {
    // ❌ ERROR: parse is not public
    let result = my_project::parser::parse("test");
}
```

Solution: Make items public at ALL levels:
```rust
// src/lib.rs
pub mod parser {
    pub fn parse(input: &str) -> String {  // Both pub
        input.to_uppercase()
    }
}
```

```rust
#[test]
fn works() {
    let result = my_project::parser::parse("test");  // ✅
}
```

