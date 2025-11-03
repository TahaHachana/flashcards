## Parser State Machine Pattern

What lifetime pattern do parser/lexer types typically use when maintaining position in borrowed input?

```rust
struct Lexer<'a> {
    input: &'a str,
    position: usize,
}
```

---

Parsers store a reference to input data with lifetime `'a` along with position/state. Methods can return slices of the input with lifetime `'a`. This is Pattern 6 (Struct Methods with Lifetime Parameters). The struct "owns" the lifetime, and methods inherit it for returning references to portions of the input.

