## The Move Keyword

What does the `move` keyword do in closures, and when is it required?

---

The `move` keyword forces a closure to take ownership of all captured variables, even if the closure only needs to borrow them.

```rust
let x = String::from("hello");
let closure = move || println!("{}", x);
// x is now moved, can't use it here
```

**Required in two main scenarios:**

1. **Threads** - Spawned threads require owned data:
```rust
thread::spawn(move || {
    println!("{}", data); // Must own data
})
```

2. **Returning closures** - When closure outlives its environment:
```rust
fn make_adder(n: i32) -> impl Fn(i32) -> i32 {
    move |x| x + n // n must be moved
}
```

Without `move`, closures try to borrow by default.

