## Check if String is ASCII-only

How do you check if a string contains only ASCII characters?

---

```rust
// Built-in method
fn is_ascii(s: &str) -> bool {
    s.is_ascii()
}

// Manual implementation
fn is_ascii_manual(s: &str) -> bool {
    s.chars().all(|c| c.is_ascii())
}

println!("{}", is_ascii("hello"));  // true
println!("{}", is_ascii("你好"));   // false
```
ASCII-only strings have byte count equal to character count.

