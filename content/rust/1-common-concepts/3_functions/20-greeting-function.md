# Greeting Function

Write a function that takes no parameters and returns the string "Hello, Rust!"

---

```rust
fn greeting() -> String {
    String::from("Hello, Rust!")
}
```
or
```rust
fn greeting() -> &'static str {
    "Hello, Rust!"
}
```