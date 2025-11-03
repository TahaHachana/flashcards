## Pattern 5 No Output References

What lifetime considerations apply when a function uses references but doesn't return any references?

```rust
fn compare<'a, 'b>(x: &'a str, y: &'b str) -> bool {
    x.len() > y.len()
}
```

---

When return type doesn't contain references (or is `()`), input lifetimes are often independent and usually don't matter. The function only uses inputs temporarily during the call. Mental shortcut: "No references out" → lifetimes usually don't need to be related (and are often elided automatically).

