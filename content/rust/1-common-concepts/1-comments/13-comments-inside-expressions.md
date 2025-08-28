# Comments Inside Expressions

Can you put comments inside expressions or statements?

---

Yes, but it's generally not recommended as it can hurt readability:
```rust
let result = x + /* this is confusing */ y;
// Better:
// Add x and y together
let result = x + y;
```