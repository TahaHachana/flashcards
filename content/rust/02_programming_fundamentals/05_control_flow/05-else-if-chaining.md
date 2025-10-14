## else if Chaining

How do you chain multiple conditions in Rust?

---

Use else if for additional conditions. Only the first matching condition executes.

```rust
if number % 4 == 0 {
    println!("Divisible by 4");
} else if number % 2 == 0 {
    println!("Divisible by 2");
} else {
    println!("Odd");
}
```

