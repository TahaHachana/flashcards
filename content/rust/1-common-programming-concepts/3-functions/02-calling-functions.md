## Calling Functions

How do you call a function in Rust, and does its position in the source file matter?

---

Call a function by its name followed by parentheses. The function can be defined before or after the caller, as long as it is in scope.

Example:
```rust
fn main() {
    another_function();
}
```

