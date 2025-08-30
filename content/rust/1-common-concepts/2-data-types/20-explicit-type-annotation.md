# Explicit Type Annotation

How do you explicitly annotate a variable's type when the compiler can't infer it?

---

Use type annotation with colon syntax:
```rust
let guess: u32 = "42".parse().expect("Not a number!");
```
Without the `: u32`, the compiler wouldn't know which numeric type to use.