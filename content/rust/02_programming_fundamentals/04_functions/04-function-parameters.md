## Function Parameters

How do you define function parameters in Rust?

---

Use name: type syntax. Type annotations are required for parameters.

```rust
fn greet(name: &str) {
    println!("Hello, {}!", name);
}
greet("Alice");
```

