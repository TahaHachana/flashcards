## Named vs Anonymous Closures

What's the difference between named and anonymous closures? When would you use each?

---

**Named closures** are assigned to variables:
```rust
let double = |x| x * 2;
let result = double(5);
```

**Anonymous closures** are used directly as arguments:
```rust
vec![1, 2, 3].iter().map(|x| x * 2).collect()
```

**When to use named:**
- Need to call the closure multiple times
- Closure is complex and deserves a descriptive name
- Want to reuse the same logic
- Debugging is easier with a name

**When to use anonymous:**
- One-time use (most common in iterator chains)
- Simple, self-explanatory operation
- Keeping code concise and readable
- Common with `map`, `filter`, `for_each`

Most Rust code uses anonymous closures for simple transformations and named closures for reused or complex logic.

