## Static Typing

What does it mean that Rust is a statically typed language?

---

All variable types must be known at compile time.  
The compiler can often infer types, but explicit annotations are needed when multiple types are possible.

```rust
let guess: u32 = "42".parse().expect("Not a number!");
```

