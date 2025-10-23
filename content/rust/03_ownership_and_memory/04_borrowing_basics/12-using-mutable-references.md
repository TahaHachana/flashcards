## Using Mutable References

What can you do with a mutable reference?

---

Both read and modify the borrowed data.

```rust
fn append(s: &mut String) {
    s.push_str(" world");
}
let mut s = String::from("hello");
append(&mut s);  // s is now "hello world"
```

