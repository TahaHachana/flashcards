## Iterating Over Slices

How do you iterate over a slice?

---

Use for loop directly or with iter() for more control.

```rust
for &num in slice {
    println!("{}", num);
}

for (i, &num) in slice.iter().enumerate() {
    println!("Index {}: {}", i, num);
}
```

