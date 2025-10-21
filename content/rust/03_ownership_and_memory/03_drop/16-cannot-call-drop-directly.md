## Cannot Call drop Directly

Can you call .drop() method directly on a value?

---

No. Explicit destructor calls aren't allowed. Use std::mem::drop instead.

```rust
s.drop();  // ❌ Error
drop(s);   // ✅ OK
```

