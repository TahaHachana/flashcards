## Preventing RefCell Panics

What are five strategies to prevent RefCell panics?

---

**Strategy 1: Immediate mutation (no variables)**
```rust
// ✅ Guard dropped immediately
*cell.borrow_mut() = vec![1, 2, 3];
*cell.borrow_mut() = vec![4, 5, 6];  // Safe - no conflict
```

**Strategy 2: Explicit scopes**
```rust
{
    let mut borrow = cell.borrow_mut();
    borrow.push(1);
}  // Guard dropped here

cell.borrow_mut().push(2);  // Safe now
```

**Strategy 3: Use try_ methods**
```rust
match cell.try_borrow_mut() {
    Ok(mut data) => {
        data.push(1);
    }
    Err(_) => {
        println!("Already borrowed, skipping");
        // Handle gracefully
    }
}
```

**Strategy 4: Separate borrows**
```rust
// ❌ Bad: double borrow
cell.borrow_mut().push(*cell.borrow().first().unwrap());

// ✅ Good: separate
let first = *cell.borrow().first().unwrap();
cell.borrow_mut().push(first);
```

**Strategy 5: Explicit drops**
```rust
let mut borrow = cell.borrow_mut();
borrow.push(1);
drop(borrow);  // Explicitly release

cell.borrow();  // Safe now
```

**Golden rule:** If no variables hold the guard, you can't panic.

