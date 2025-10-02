## Default Enum Variant

How do you specify a default enum variant?

---

Mark a variant with `#[default]` and derive `Default`:

```rust
#[derive(Default)]
enum Mode {
    #[default]
    Normal,
    Insert,
    Visual,
}
```

