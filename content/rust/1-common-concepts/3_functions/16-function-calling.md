# Function Calling

How do you call a function in Rust?

---

Use the function name followed by parentheses with arguments if needed:
```rust
fn main() {
    greet(); // No arguments
    add(5, 3); // With arguments
    let result = multiply(4, 2); // Capture return value
}
```