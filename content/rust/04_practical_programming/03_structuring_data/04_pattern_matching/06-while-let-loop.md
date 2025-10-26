## while let Loop

What does while let do and when is it useful?

---

**while let** loops as long as a pattern continues to match:

```rust
let mut stack = vec![1, 2, 3];

while let Some(top) = stack.pop() {
    println!("{}", top);
}
// Prints: 3, 2, 1
```

More concise than:
```rust
loop {
    match stack.pop() {
        Some(top) => println!("{}", top),
        None => break,
    }
}
```

**Useful for**:
- Processing iterators until exhausted
- Popping from collections until empty
- Any loop that continues while a pattern matches

The loop ends when the pattern no longer matches.

