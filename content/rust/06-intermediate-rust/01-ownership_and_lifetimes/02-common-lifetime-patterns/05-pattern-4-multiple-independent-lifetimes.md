## Pattern 4 Multiple Independent Lifetimes

When should you use different lifetime parameters (`'a` and `'b`) for different inputs?

```rust
fn search_with_default<'a, 'b>(
    data: &'a [i32],
    target: i32,
    default: &'b i32
) -> &'a i32
```

---

Use different lifetimes when the return depends on only one input, or when inputs have independent validity requirements. This is more flexible for callers than requiring all inputs to have the same lifetime. Mental shortcut: "Some inputs are side channels" → separate lifetimes. Use when some inputs are only used during the function call, not returned.

