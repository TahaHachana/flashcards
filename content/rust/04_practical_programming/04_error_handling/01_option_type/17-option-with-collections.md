## Option With Collections

How can you filter out `None` values from a `Vec<Option<T>>`?

---

Use `.flatten()` on the iterator:

```rust
let numbers: Vec<Option<i32>> = vec![Some(1), None, Some(3)];
let valid: Vec<i32> = numbers.into_iter().flatten().collect();
// [1, 3]
```

Alternatively, collect into `Option<Vec<T>>` to fail if any element is `None`:

```rust
let all_some = vec![Some(1), Some(2), Some(3)];
let result: Option<Vec<i32>> = all_some.into_iter().collect();
// Some([1, 2, 3])
```

