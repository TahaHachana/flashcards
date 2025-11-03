## Gotcha Function Return Type Must Specify Lifetime

Why won't this compile, and what's needed?
```rust
fn create_parser(text: &str) -> Parser {
    Parser { input: text }
}
```

---

The function signature doesn't specify how the returned `Parser`'s lifetime relates to `text`. Fix:
```rust
fn create_parser<'a>(text: &'a str) -> Parser<'a> {
    Parser { input: text }
}
```
This makes explicit that the returned Parser has the same lifetime as the input text it borrows from.

