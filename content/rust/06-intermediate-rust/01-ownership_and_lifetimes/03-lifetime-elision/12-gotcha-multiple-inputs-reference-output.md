## Gotcha Multiple Inputs Reference Output

Why doesn't elision work for this function, and what's needed?

```rust
fn choose(x: &str, y: &str, condition: bool) -> &str {
    if condition { x } else { y }
}
```

---

After Rule 1, inputs have separate lifetimes `'a` and `'b`. Rules 2 and 3 don't apply (multiple inputs, not a method). The compiler can't determine which input's lifetime the output should have. Fix with explicit annotations:
```rust
fn choose<'a>(x: &'a str, y: &'a str, condition: bool) -> &'a str
```
This explicitly states the output could come from either input.

