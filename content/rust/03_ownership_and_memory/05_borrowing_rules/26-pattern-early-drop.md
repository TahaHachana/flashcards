## Pattern Early Drop

How do you end a borrow before the natural scope ends?

---

Use explicit scope blocks to end borrows early.

```rust
{
    let r = &data[..];
    println!("{:?}", r);
}  // Borrow ends explicitly
data.push(4);
```

