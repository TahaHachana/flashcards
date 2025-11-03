## When Elision Fails

What happens when the three elision rules cannot determine all lifetimes in a signature?

---

If after applying all three rules any output lifetime remains unresolved, the compiler requires explicit annotations. Example:
```rust
// ❌ Won't compile - ambiguous
fn longest(x: &str, y: &str) -> &str

// After Rule 1: separate lifetimes for x and y
// Rules 2 and 3 don't apply (multiple inputs, not a method)
// Output lifetime still unknown → ERROR

// ✅ Explicit annotation required
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str
```

