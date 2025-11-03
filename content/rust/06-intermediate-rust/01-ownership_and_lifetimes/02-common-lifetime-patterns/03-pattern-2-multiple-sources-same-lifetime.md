## Pattern 2 Multiple Sources Same Lifetime

When should you use the same lifetime `'a` for multiple inputs and the return value?

```rust
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() { x } else { y }
}
```

---

Use this pattern when the return could come from any of multiple inputs, so all must live at least as long as the return value. The compiler enforces that all inputs must live at least as long as `'a`. Mental shortcut: "Output could be any input" → all same lifetime. This is more restrictive than Pattern 1, so use Pattern 1 if possible.

