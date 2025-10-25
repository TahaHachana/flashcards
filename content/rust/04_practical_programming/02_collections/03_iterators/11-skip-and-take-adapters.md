## Skip and Take Adapters

What do `.skip(n)` and `.take(n)` do? Give an example.

---

- `.skip(n)`: Skip first n items
- `.take(n)`: Take next n items

```rust
let result: Vec<i32> = vec![0,1,2,3,4,5,6,7]
    .iter()
    .skip(3)   // Skip [0,1,2]
    .take(4)   // Take [3,4,5,6]
    .cloned()
    .collect();
// result = [3, 4, 5, 6]
```

