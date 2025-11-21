## When to Use Each Fn Trait

When should a function parameter require `Fn`, `FnMut`, or `FnOnce`? Provide decision criteria.

---

Choose based on how many times you call the closure and what it needs to do:

**Use `FnOnce` when:**
- Calling the closure only once
- Maximum flexibility (accepts any closure)
- Closure might consume captured values
```rust
fn call_once<F: FnOnce()>(f: F) {
    f(); // Called exactly once
}
```

**Use `FnMut` when:**
- Calling the closure multiple times
- Closure needs to mutate captured variables
- Iterator methods like `map`, `filter`
```rust
fn call_multiple<F: FnMut(i32)>(mut f: F, data: &[i32]) {
    for &x in data {
        f(x); // Called multiple times, may mutate
    }
}
```

**Use `Fn` when:**
- Calling the closure multiple times
- Closure is pure (no mutation)
- Need to call from multiple threads
- Most restrictive, but most flexible usage
```rust
fn call_many_times<F: Fn()>(f: F) {
    f(); f(); f(); // Pure closure, no mutation
}
```

**Rule of thumb:** Start with `FnOnce`, restrict to `FnMut` or `Fn` only if needed.

