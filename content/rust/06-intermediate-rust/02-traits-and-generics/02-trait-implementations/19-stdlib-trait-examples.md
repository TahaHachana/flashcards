## Standard Library Trait Examples

Name three commonly implemented standard library traits and their purposes.

---

1. **Display** (`std::fmt::Display`) - Formatting with `{}`, user-facing output
2. **Debug** (`std::fmt::Debug`) - Formatting with `{:?}`, programmer-facing debugging
3. **From/Into** - Type conversions between types
4. **Clone** - Explicit duplication of values
5. **PartialEq/Eq** - Equality comparisons with `==`

Example:
```rust
impl Display for MyType { /* ... */ }
impl From<String> for MyType { /* ... */ }
impl Clone for MyType { /* ... */ }
```

