## Tuple Iteration

Can you iterate over tuples directly in a for loop?

---

No. Tuples are not directly iterable. Arrays can be iterated but tuples cannot.

```rust
let tup = (1, 2, 3);
for x in tup { }  // ❌ Error

let arr = [1, 2, 3];
for x in arr { }  // ✅ OK
```

