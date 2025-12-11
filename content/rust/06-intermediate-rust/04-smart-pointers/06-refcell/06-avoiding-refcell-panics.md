## Avoiding RefCell Panics

What are three strategies to avoid panics when using `RefCell`?

---

**Strategy 1: Immediate mutation (no variables)**
```rust
// ✅ Safe: borrow guard dropped immediately
*cell.borrow_mut() = 10;
*cell.borrow_mut() = 20;  // No conflict - first borrow already dropped
```

**Strategy 2: Explicit scopes**
```rust
{
    let mut borrow = cell.borrow_mut();
    *borrow = 10;
}  // borrow dropped here

// Now can borrow again
let borrow2 = cell.borrow_mut();
```

**Strategy 3: Use try_ methods**
```rust
if let Ok(mut value) = cell.try_borrow_mut() {
    *value = 10;
} else {
    println!("Couldn't borrow, skipping");
    // Handle gracefully instead of panicking
}
```

**Best practices:**
- Keep borrows short-lived
- Drop guards explicitly when done
- Use `try_` methods when unsure
- Avoid storing `Ref`/`RefMut` guards in structs

**Golden rule:** If no variables hold the guard, you can't panic.

