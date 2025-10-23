## Borrowing in Loops

How do you borrow elements when iterating?

---

Use & to borrow immutably or &mut to borrow mutably.

```rust
for s in &strings {  // Borrow each
    println!("{}", s);
}
for s in &mut strings {  // Mutable borrow
    s.push_str("!");
}
```

