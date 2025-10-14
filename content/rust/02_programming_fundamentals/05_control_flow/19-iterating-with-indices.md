## Iterating with Indices

How do you get both index and value when iterating?

---

Use enumerate() on the iterator.

```rust
let arr = [10, 20, 30];
for (index, value) in arr.iter().enumerate() {
    println!("arr[{}] = {}", index, value);
}
```

