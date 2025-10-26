## What Is Pattern Matching?

What is pattern matching in Rust and what three operations does it combine into one?

---

Pattern matching compares a value against a series of patterns and executes code based on which pattern matches.

**Three operations combined**:
1. **Testing** if a value matches a pattern
2. **Destructuring** the value to extract parts
3. **Binding** those parts to variables

```rust
match point {
    (0, 0) => println!("origin"),           // Test exact values
    (x, 0) => println!("x-axis at {}", x),  // Extract and bind x
    (x, y) => println!("at ({}, {})", x, y), // Extract both
}
```

More powerful than simple conditionals because it can destructure complex types in a single expression.

