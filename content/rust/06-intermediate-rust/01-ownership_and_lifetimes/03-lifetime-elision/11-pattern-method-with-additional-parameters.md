## Pattern Method with Additional Parameters

Does Rule 3 still apply when a method has additional reference parameters beyond `&self`?

```rust
impl Parser {
    fn parse_with_default(&self, default: &str) -> &str {
        self.current_token()
    }
}
```

---

Yes, Rule 3 applies even with multiple inputs. It prioritizes `self`'s lifetime for outputs. Expanded:
```rust
impl Parser {
    fn parse_with_default<'a, 'b>(&'a self, default: &'b str) -> &'a str
```
The returned reference is tied to `self`'s lifetime, not `default`'s lifetime.

