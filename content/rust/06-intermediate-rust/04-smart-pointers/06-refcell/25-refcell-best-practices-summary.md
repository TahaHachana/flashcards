## RefCell Best Practices Summary

Summarize the best practices for using `RefCell` effectively and safely.

---

**1. Prefer compile-time safety:**
```rust
// ✅ Try this first
let mut data = vec![1, 2, 3];

// Only if API requires &self
let data = RefCell::new(vec![1, 2, 3]);
```

**2. Keep borrows short:**
```rust
// ❌ Bad - long-lived guard
let guard = cell.borrow();
do_lots_of_work();
use_guard(&guard);

// ✅ Good - minimal lifetime
{
    let guard = cell.borrow();
    use_guard(&guard);
}
do_lots_of_work();
```

**3. Don't store guards:**
```rust
// ❌ Don't store Ref/RefMut
struct Holder<'a> {
    guard: Ref<'a, Data>,
}

// ✅ Store RefCell
struct Holder {
    cell: RefCell<Data>,
}
```

**4. Use try_ methods when unsure:**
```rust
// ✅ Safe - won't panic
if let Ok(mut data) = cell.try_borrow_mut() {
    data.update();
}
```

**5. Immediate mutations need no variables:**
```rust
// ✅ Safe - guard immediately dropped
*cell.borrow_mut() = new_value;
```

**6. Combine with Rc for shared mutable state:**
```rust
// ✅ Standard pattern
let shared = Rc::new(RefCell::new(data));
```

**7. Document why you're using RefCell:**
```rust
/// Uses RefCell because Logger trait requires &self
struct FileLogger {
    logs: RefCell<Vec<String>>,
}
```

**Golden rules:**
- Use only when necessary
- Keep borrows short
- Use try_ methods in uncertain contexts
- Test thoroughly (runtime checks!)
- Document the rationale

