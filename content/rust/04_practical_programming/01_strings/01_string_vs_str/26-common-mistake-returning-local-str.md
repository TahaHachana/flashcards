## Common Mistake - Returning Local &str

Why is this function wrong and how do you fix it?
```rust
fn get_hello() -> &str {
    let s = String::from("hello");
    &s
}
```

---

This returns a reference to a local variable that will be dropped. The &str would be dangling. Fix by returning owned String:
```rust
fn get_hello() -> String {
    String::from("hello")  // Returns owned String
}
```
The caller receives ownership and the data remains valid.

