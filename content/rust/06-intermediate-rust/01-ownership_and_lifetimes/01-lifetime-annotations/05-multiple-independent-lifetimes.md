## Multiple Independent Lifetimes

When and why would you use multiple lifetime parameters like `'a` and `'b` in a function signature?

---

You use multiple lifetime parameters when the return lifetime depends on only one input, or when inputs have independent validity requirements. Example:
```rust
fn first_word<'a, 'b>(x: &'a str, _y: &'b str) -> &'a str
```
This tells the caller that the return lifetime matches only `x`, not `y`. This is less restrictive than requiring both parameters to have the same lifetime.

