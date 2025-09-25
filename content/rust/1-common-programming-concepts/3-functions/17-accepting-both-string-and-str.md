## Accepting Both String and &str

How can you write a function that accepts both `String` and `&str`?

---

Use a generic parameter with the `AsRef<str>` trait.

Example:

```rust
fn greet<S: AsRef<str>>(name: S) {
    println!("Hello, {}", name.as_ref());
}
```

