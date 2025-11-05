## Why Compiler Can't Guess Implementation

Why can't Rust automatically implement traits like `Add` for your types, requiring you to do it manually?

---

The compiler can't guess your intended behavior. For a type with multiple fields, there are many ways to implement addition:

```rust
struct Point {
    x: i32,
    y: i32,
}
```

Should `+` add x-to-x and y-to-y? Add all fields together? Concatenate them as strings? Only add x values? The compiler has no way to know your intent, so you must explicitly define the behavior.

