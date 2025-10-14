## Best Practice - Prefer for Over while

Why should you prefer for loops over while loops for iteration?

---

for loops are more idiomatic, prevent common bugs (off-by-one, out-of-bounds), clearly express intent, and are more concise.

```rust
// Less idiomatic
let mut i = 0;
while i < 10 {
    println!("{}", i);
    i += 1;
}

// More idiomatic
for i in 0..10 {
    println!("{}", i);
}
```

