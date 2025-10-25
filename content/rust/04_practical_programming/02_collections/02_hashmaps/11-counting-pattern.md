## Counting Pattern

Write code to count occurrences of each word in a Vec using HashMap.

---

```rust
let words = vec!["apple", "banana", "apple"];
let mut counts = HashMap::new();

for word in words {
    let count = counts.entry(word).or_insert(0);
    *count += 1;  // Dereference to modify
}
// counts: {"apple": 2, "banana": 1}
```

