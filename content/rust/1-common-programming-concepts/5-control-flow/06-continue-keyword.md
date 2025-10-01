## Continue Keyword

What does the `continue` keyword do inside a loop?

---

It skips the current iteration and moves directly to the next one.

```rust
for i in 1..5 {
    if i == 3 { continue; }
    println!("{i}");
}
```

