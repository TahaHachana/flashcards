## Filtering Into New Vector

Given `let nums = vec![1,2,3,4,5,6];`, create a new vector with only even numbers using a loop.

---

```rust
let nums = vec![1, 2, 3, 4, 5, 6];
let mut evens = Vec::new();
for &num in &nums {
    if num % 2 == 0 {
        evens.push(num);
    }
}
// evens = [2, 4, 6]
```

