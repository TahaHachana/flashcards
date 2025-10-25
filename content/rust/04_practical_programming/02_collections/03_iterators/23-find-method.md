## Find Method

What does `.find()` return and how is it different from `.filter()`?

---

`.find()` returns `Option<T>` with the **first** matching item, then stops:
```rust
let result = vec.iter().find(|&&x| x > 5);
// Some(&6) if found, None if not
```

`.filter()` returns an iterator of **all** matching items:
```rust
let results: Vec<i32> = vec.iter()
    .filter(|&&x| x > 5)
    .cloned()
    .collect();
```

