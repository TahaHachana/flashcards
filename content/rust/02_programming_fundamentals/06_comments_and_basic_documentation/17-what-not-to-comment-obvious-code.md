## What Not to Comment - Obvious Code

Should you comment obvious operations?

---

No. Don't comment code that's self-explanatory.

```rust
// BAD: Adds no value
// Increment i
i += 1;

// GOOD: No comment - code is clear
i += 1;
```

