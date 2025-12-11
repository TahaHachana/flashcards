## Gotcha - Arc Doesn't Make T Thread-Safe

Can you put any type `T` inside `Arc<T>` and send it across threads? What's the rule?

---

**The gotcha:**
```rust
use std::sync::Arc;
use std::rc::Rc;
use std::thread;

// ❌ This won't compile
let arc_rc = Arc::new(Rc::new(5));
thread::spawn(move || {
    println!("{}", arc_rc);
});
```

**Error:**
```
error[E0277]: `Rc<i32>` cannot be sent between threads safely
   |
   = help: the trait `Send` is not implemented for `Rc<i32>`
```

**The rule:** `Arc<T>` is only thread-safe if `T` is thread-safe (implements `Send`).

**Why?** 
- `Arc` makes the **pointer** thread-safe
- But not the **data** inside
- If `T` isn't `Send`, you can't send it between threads
- Compiler prevents this at compile time

**Examples:**
```rust
// ✅ Works: i32 implements Send
let arc = Arc::new(5);
thread::spawn(move || { });

// ✅ Works: String implements Send  
let arc = Arc::new(String::from("hello"));
thread::spawn(move || { });

// ❌ Fails: Rc doesn't implement Send
let arc = Arc::new(Rc::new(5));
thread::spawn(move || { });  // Compile error

// ❌ Fails: RefCell doesn't implement Sync
let arc = Arc::new(RefCell::new(5));
thread::spawn(move || { });  // Compile error
```

**Key insight:** Arc provides thread-safe sharing, but T must be thread-safe itself.

