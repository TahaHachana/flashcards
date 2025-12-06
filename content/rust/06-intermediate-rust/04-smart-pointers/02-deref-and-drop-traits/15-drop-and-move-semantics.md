## Drop and Move Semantics

What happens to `Drop` when a value is moved? Demonstrate with an example.

---

**When a value is moved, `Drop` is NOT called on the original location:**

```rust
struct Loud;

impl Drop for Loud {
    fn drop(&mut self) {
        println!("Dropping!");
    }
}

fn main() {
    let x = Loud;
    let y = x;  // x moved to y, x.drop() is NOT called
    
    // Only y.drop() is called when y goes out of scope
}
```

**Output:**
```
Dropping!
```

Only **one** "Dropping!" is printed, for `y`.

**Why:** After the move, `x` is considered uninitialized. Only the current owner (`y`) has its drop called. This prevents double-free errors.

**Key insight:** Drop follows ownership. Only the current owner's drop is called.

