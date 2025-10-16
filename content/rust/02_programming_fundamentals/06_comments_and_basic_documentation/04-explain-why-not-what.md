## Explain Why Not What

Should comments describe what the code does or why it exists?

---

Explain why, not what. What the code does should be clear from the code itself.

```rust
// BAD: Add 1 to x
x = x + 1;

// GOOD: Increment by 1 to account for zero-indexing
x = x + 1;
```

