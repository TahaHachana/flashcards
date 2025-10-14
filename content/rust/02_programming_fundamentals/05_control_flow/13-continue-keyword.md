## continue Keyword

How do you skip the rest of the current iteration and start the next one?

---

Use the continue keyword.

```rust
for i in 1..10 {
    if i % 2 == 0 {
        continue;  // Skip even numbers
    }
    println!("{}", i);  // Only prints odd
}
```

