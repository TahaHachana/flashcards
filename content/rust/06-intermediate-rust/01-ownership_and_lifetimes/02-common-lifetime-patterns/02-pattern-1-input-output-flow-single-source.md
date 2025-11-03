## Pattern 1 Input-Output Flow Single Source

What characterizes the "Input-Output Flow (Single Source)" pattern, and when should you use it?

```rust
fn first_element<'a>(data: &'a [i32]) -> &'a i32 {
    &data[0]
}
```

---

Characteristics: One reference input with lifetime `'a`, return type has same lifetime `'a`, other inputs (if any) have independent lifetimes or are values. Use when output is clearly extracted from one specific input. Mental shortcut: "Output points into input" → same lifetime.

