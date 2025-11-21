## Closure Best Practices Summary

What are the key best practices when working with closures in Rust?

---

**1. Prefer borrowing over moving:**
- Let compiler choose capture mode
- Only use `move` when necessary (threads, returning closures)

**2. Use anonymous closures for simple, one-time operations:**
```rust
numbers.iter().filter(|&x| x > 0).collect()
```

**3. Name complex closures:**
```rust
let is_valid_user = |user: &User| {
    user.age >= 18 && user.verified
};
```

**4. Choose the right Fn trait:**
- Default to `FnOnce` for maximum flexibility
- Use `FnMut` when mutation needed
- Use `Fn` for pure operations

**5. Avoid returning closures when possible:**
- Prefer functions or impl Trait
- Use closures for local, inline logic

**6. Pattern match in parameters:**
```rust
points.iter().for_each(|&Point { x, y }| /* ... */)
```

**7. Keep closures small and focused:**
- Extract complex logic to functions
- Closures shine with 1-3 line operations

**8. Remember closure type uniqueness:**
- Each closure is a distinct type
- Can't compare closures directly

**9. Use type annotations sparingly:**
- Let type inference work
- Add types only when compiler can't figure it out

**10. Don't fight the borrow checker:**
- If captures are complex, consider refactoring
- Sometimes a regular function is clearer

