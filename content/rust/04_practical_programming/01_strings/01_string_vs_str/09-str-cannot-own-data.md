## &str Cannot Own Data

Why does this function produce an error?
```rust
fn get_slice() -> &str {
    let s = String::from("hello");
    &s[..]
}
```

---

The function returns an error because &str doesn't own data. The String s is dropped when the function ends, so returning &str would create a dangling reference pointing to freed memory. The &str would outlive the data it references, violating Rust's lifetime rules.

