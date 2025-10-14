## if Condition Must Be Bool

Can you use non-boolean values as if conditions in Rust?

---

No. Conditions must be bool type. Rust won't automatically convert other types.

```rust
if number { }  // ❌ Error
if number != 0 { }  // ✅ OK: explicitly bool
```

