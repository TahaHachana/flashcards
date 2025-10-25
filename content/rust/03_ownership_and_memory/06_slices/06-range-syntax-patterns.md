## Range Syntax Patterns

What are the range syntax patterns for slices?

---

[start..end] (exclusive end), [..end] (from beginning), [start..] (to end), [..] (entire sequence).

```rust
&s[0..5]  // From 0 to 5
&s[..5]   // From start to 5
&s[3..]   // From 3 to end
&s[..]    // Entire string
```

