## Iterator Invalidation Prevention

How does the borrow checker prevent iterator invalidation?

---

Can't modify a collection while iterating. Common bug in C++.

```rust
for item in &vec {
    vec.push(*item);  // ❌ Error: can't modify while iterating
}
```

