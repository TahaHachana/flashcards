## Mixing Thread-Safe and Non-Thread-Safe

What happens if you try to put a non-thread-safe type inside `Arc`? Show the error and explanation.

---

**The problem:**
```rust
use std::sync::Arc;
use std::rc::Rc;
use std::thread;

// ❌ Won't compile
let arc_rc = Arc::new(Rc::new(5));
thread::spawn(move || {
    println!("{}", arc_rc);
});
```

**Compiler error:**
```
error[E0277]: `Rc<i32>` cannot be sent between threads safely
   |
   = help: the trait `Send` is not implemented for `Rc<i32>`
```

**Why?**
- `Arc` makes the **pointer** thread-safe
- But not the **data** inside
- If `T` doesn't implement `Send`, you can't send it between threads
- Compiler prevents this at compile time

**Valid combinations:**
```rust
// ✅ Arc with thread-safe types
Arc::new(5)                    // i32 is Send
Arc::new(String::from("hi"))   // String is Send
Arc::new(Mutex::new(5))        // Mutex<i32> is Send

// ❌ Arc with non-thread-safe types
Arc::new(Rc::new(5))           // Rc is not Send
Arc::new(RefCell::new(5))      // RefCell is not Send/Sync
```

**Rule:** `Arc<T>` is only thread-safe if `T` implements `Send` (and `Sync` for shared access).

**Fix for shared state across threads:**
```rust
// Instead of Arc<RefCell<T>>
// Use Arc<Mutex<T>>
let data = Arc::new(Mutex::new(5));
```

