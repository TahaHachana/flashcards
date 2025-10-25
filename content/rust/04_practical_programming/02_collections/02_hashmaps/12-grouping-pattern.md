## Grouping Pattern

How do you group items into a Vec using the entry API? Show the pattern for grouping ratings by gender.

---

```rust
let data = vec![("male", 9), ("female", 5), ("male", 10)];
let mut groups = HashMap::new();

for (gender, rating) in data {
    groups.entry(gender)
          .or_insert(Vec::new())
          .push(rating);
}
// {"male": [9, 10], "female": [5]}
```

