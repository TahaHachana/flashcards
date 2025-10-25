## Empty Vector Pattern

Write a while loop that repeatedly pops from a vector and prints values until empty.

---

```rust
let mut vec = vec![1, 2, 3, 4, 5];
while let Some(val) = vec.pop() {
    println!("{}", val);
}
// Prints 5, 4, 3, 2, 1
```

