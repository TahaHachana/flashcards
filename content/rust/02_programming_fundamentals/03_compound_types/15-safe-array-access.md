## Safe Array Access

How do you safely access an array element that might be out of bounds?

---

Use the get method which returns an Option instead of panicking.

```rust
let arr = [1, 2, 3];
match arr.get(10) {
    Some(val) => println!("Value: {}", val),
    None => println!("Out of bounds"),
}
```

