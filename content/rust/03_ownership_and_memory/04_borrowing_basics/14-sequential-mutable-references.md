## Sequential Mutable References

Can you have multiple mutable references if they don't overlap?

---

Yes. As long as they're not active at the same time.

```rust
let mut s = String::from("hello");
{
    let r1 = &mut s;
}  // r1 gone
let r2 = &mut s;  // ✅ OK
```

