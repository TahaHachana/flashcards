## Single Writer Pattern

Why can only one function borrow data mutably at a time?

---

Exclusive mutable access prevents data races. Only one part of code can modify data, preventing conflicts and unpredictable behavior.

```rust
fn modify(s: &mut String) {
    s.push_str("!");
}
```

