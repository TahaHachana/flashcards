## What Not to Comment - Paraphrasing

Should comments paraphrase what the code does?

---

No. Comments should explain why, not repeat what the code already shows.

```rust
// BAD: Just repeats code
// Loop through all users
for user in users { }

// GOOD: Explains purpose
// Send welcome emails to new users
for user in users { }
```

