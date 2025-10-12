## Iterating Over Arrays

How do you iterate over an array?

---

Use a for loop directly, or use iter() with enumerate() for indices.

```rust
let arr = [10, 20, 30];
for element in arr {
    println!("{}", element);
}

for (i, val) in arr.iter().enumerate() {
    println!("arr[{}] = {}", i, val);
}
```

