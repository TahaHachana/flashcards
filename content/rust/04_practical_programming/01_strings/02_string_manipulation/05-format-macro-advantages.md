## Format Macro Advantages

Why is format! better than + for concatenating multiple strings? What are its advantages?

---

```rust
let s = format!("{}-{}-{}", s1, s2, s3);
```
Advantages:
1. All arguments are borrowed (nothing moved) - all original strings remain valid
2. Clearer, more readable syntax
3. More flexible - can include other types, not just strings
4. Better for multiple concatenations

Unlike +, format! doesn't take ownership of any arguments.

