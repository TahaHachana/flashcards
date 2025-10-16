## Don't Comment Out Code

Why shouldn't you comment out old code?

---

Use version control (git) instead. Commented code clutters the codebase. Delete old code and use git history if needed.

```rust
// BAD: Clutters codebase
// fn old_implementation() { }

// GOOD: Delete and use git history
fn new_implementation() { }
```

