## Rust Type System Basics

What does it mean that Rust is statically typed, and when is a type annotation required?

---

Rust is statically typed, meaning all variable types must be known at compile time.  
The compiler can usually infer types, but annotations are required when:

- Multiple types are possible (ambiguity).
- Using generic methods like `parse()`.
- You want a type other than the default (`i32` for integers, `f64` for floats).

Example:
```rust
let guess: u32 = "42".parse().expect("Not a number!");
```

