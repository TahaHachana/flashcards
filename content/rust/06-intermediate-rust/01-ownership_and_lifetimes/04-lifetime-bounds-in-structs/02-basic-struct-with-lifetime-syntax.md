## Basic Struct with Lifetime Syntax

What does this struct definition mean?
```rust
struct Excerpt<'a> {
    text: &'a str,
}
```

---

This means: `'a` is a generic lifetime parameter (like `<T>` for types), the field `text` is a reference with lifetime `'a`, and any instance of `Excerpt<'a>` cannot outlive `'a`. The struct can only exist while the data it references remains valid.

