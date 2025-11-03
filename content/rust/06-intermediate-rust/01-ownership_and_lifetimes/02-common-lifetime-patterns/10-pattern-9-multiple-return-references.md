## Pattern 9 Multiple Return References

When returning multiple references (tuple or struct), what lifetime pattern is typically used?

```rust
fn split_first<'a>(data: &'a [i32]) -> Option<(&'a i32, &'a [i32])> {
    data.split_first()
}
```

---

All returned references typically share the same lifetime from the same source. Used for splitting, partitioning, or decomposing borrowed data. Mental shortcut: "All pieces from same whole" → same lifetime for all. When returning references together, they need to share a lifetime so the caller knows how long the entire return value is valid.

