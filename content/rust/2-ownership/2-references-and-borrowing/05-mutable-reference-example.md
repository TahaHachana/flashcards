## Mutable Reference Example

How do you create and use a mutable reference in Rust?

---

Use `&mut` to borrow mutably.

```rust
fn change(s: &mut String) {
    s.push_str(", world");
}

let mut s = String::from("hello");
change(&mut s);
```

