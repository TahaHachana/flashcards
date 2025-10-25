## Building Vector in Loop

Create a vector containing squares of numbers from 1 to 10 using a for loop.

---

```rust
let mut squares = Vec::new();
for i in 1..=10 {
    squares.push(i * i);
}
// squares = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

