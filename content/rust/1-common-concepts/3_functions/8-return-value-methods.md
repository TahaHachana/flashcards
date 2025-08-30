# Return Value Methods

What are the two ways to return a value from a function in Rust?

---
1. **Implicit return**: The last expression without a semicolon
   ```rust
   fn plus_one(x: i32) -> i32 {
       x + 1  // No semicolon
   }
   ```
2. **Explicit return**: Using the `return` keyword (typically for early returns)
   ```rust
   return x + 1;
   ```
