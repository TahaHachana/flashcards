## while Loops

How do you create a loop that runs while a condition is true?

---

Use a while loop with a boolean condition.

```rust
let mut number = 3;
while number != 0 {
    println!("{}!", number);
    number -= 1;
}
```

