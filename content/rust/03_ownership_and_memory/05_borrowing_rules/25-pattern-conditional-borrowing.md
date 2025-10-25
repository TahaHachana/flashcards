## Pattern Conditional Borrowing

How do you limit a borrow to only where it's needed?

---

Use scopes or conditionals to borrow only in the specific scope.

```rust
if data.len() > 2 {
    let slice = &data[0..2];
    println!("{:?}", slice);
}  // Borrow ends
data.push(4);
```

