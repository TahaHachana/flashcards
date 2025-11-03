## Impl Blocks Must Match Struct Lifetimes

What's wrong with this impl block, and how do you fix it?
```rust
struct Parser<'a> {
    input: &'a str,
}

impl Parser {
    fn new(input: &str) -> Self {
        Parser { input }
    }
}
```

---

The impl block is missing the lifetime parameter. It must match the struct definition:
```rust
impl<'a> Parser<'a> {
    fn new(input: &'a str) -> Self {
        Parser { input }
    }
}
```
The `<'a>` after `impl` declares the lifetime, and `Parser<'a>` specifies which struct this implements for.

