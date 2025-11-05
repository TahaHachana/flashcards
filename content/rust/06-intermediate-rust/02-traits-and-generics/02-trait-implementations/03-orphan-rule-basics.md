## The Orphan Rule - Three Rules

What are the three implementation scenarios allowed by the orphan rule, and what is NOT allowed?

---

**Allowed**:
1. Your trait on your type ✅
2. Your trait on external type ✅
3. External trait on your type ✅

**NOT allowed**:
4. External trait on external type ❌

Example of violation:
```rust
impl Display for Vec<i32> { }  // Error!
// Both Display and Vec are from std library
```

