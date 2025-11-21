## Closure Environment Capture Example

Explain what's happening with capture in this example:

```rust
let multiplier = 3;
let mut numbers = vec![1, 2, 3];

let transform = |x| x * multiplier;
let add_to_vec = || numbers.push(4);
```

What does each closure capture and how?

---

**First closure - `transform`:**
```rust
let transform = |x| x * multiplier;
```
- Captures `multiplier` by **immutable reference** (`&i32`)
- Only reads `multiplier`, doesn't modify it
- Implements `Fn` trait
- Can be called multiple times

**Second closure - `add_to_vec`:**
```rust
let add_to_vec = || numbers.push(4);
```
- Captures `numbers` by **mutable reference** (`&mut Vec<i32>`)
- Modifies `numbers` by pushing to it
- Implements `FnMut` trait (not `Fn`)
- Needs `mut` binding: `let mut add_to_vec = ...`
- Can be called multiple times

The compiler automatically determines the minimum necessary capture mode for each closure based on usage.

