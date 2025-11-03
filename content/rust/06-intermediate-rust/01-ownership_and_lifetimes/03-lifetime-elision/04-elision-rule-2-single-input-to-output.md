## Elision Rule 2 Single Input to Output

What is Elision Rule 2, and when does it apply?

---

Rule 2: If there's exactly one input lifetime parameter (elided or explicit), that lifetime is assigned to all elided output lifetimes.

Example:
```rust
// What you write
fn first_word(s: &str) -> &str

// What the compiler sees
fn first_word<'a>(s: &'a str) -> &'a str
```

This applies to functions with exactly one reference input. The rule exists because when there's only one input reference, any returned reference must come from it—the most common pattern.

