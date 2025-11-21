## Mutable Closure Binding

What's wrong with this code and how do you fix it?

```rust
let mut count = 0;
let increment = || count += 1;
increment();
```

---

**Problem:** Closures that mutate captured variables must themselves be bound as mutable. The closure implements `FnMut`, which requires `&mut self` to call.

**Fixed code:**
```rust
let mut count = 0;
let mut increment = || count += 1; // Added mut binding
increment();
increment();
println!("{}", count); // 2
```

**Why this is required:**
- Calling an `FnMut` closure requires a mutable reference to the closure itself
- The `mut` binding allows the compiler to obtain `&mut increment`
- This ensures exclusive access during execution

**Rule:** If your closure mutates anything, bind it with `mut`:
```rust
let mut closure = || { /* mutation code */ };
```

