## Making Custom Type Copy

How do you make a custom struct Copy?

---

Derive both Copy and Clone. The type must contain only Copy types and not implement Drop.

```rust
#[derive(Copy, Clone)]
struct Point {
    x: i32,
    y: i32,
}
```

