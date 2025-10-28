## Unwrapping User Input

Why should you never use `unwrap()` on user input?

---

**Bad - user controls whether program crashes:**
```rust
fn greet_user(name: Option<String>) {
    println!("Hello, {}!", name.unwrap());  // Panics on None!
}
```

**Good - provide default or handle error:**
```rust
fn greet_user(name: Option<String>) {
    println!("Hello, {}!", name.unwrap_or_else(|| "stranger".into()));
}
```

**Why it's wrong:**
- Users can provide invalid/missing input
- This gives users the ability to crash your program
- Violates the principle of graceful error handling
- Makes for a terrible user experience

Always validate and handle user input safely. Use `unwrap_or()`, `match`, or return `Result`.

