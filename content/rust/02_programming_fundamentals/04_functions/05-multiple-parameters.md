## Multiple Parameters

How do you define a function with multiple parameters?

---

Separate parameters with commas, each with its type annotation.

```rust
fn add(x: i32, y: i32) {
    println!("{}", x + y);
}
add(5, 3);
```

