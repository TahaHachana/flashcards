## How Rc Uses Deref and Drop

Explain how `Rc<T>` implements both `Deref` and `Drop` traits for reference counting.

---

**Deref implementation:**
```rust
impl<T> Deref for Rc<T> {
    type Target = T;
    
    fn deref(&self) -> &T {
        // Returns reference to shared data
    }
}
```

**Enables:** Accessing inner data ergonomically
```rust
let rc = Rc::new(String::from("hello"));
println!("{}", rc.len());  // Can call String methods
```

**Drop implementation:**
```rust
impl<T> Drop for Rc<T> {
    fn drop(&mut self) {
        // Decrements reference count
        // Frees memory if count reaches 0
    }
}
```

**Reference counting in action:**
```rust
use std::rc::Rc;

let rc1 = Rc::new(5);        // Count: 1
let rc2 = Rc::clone(&rc1);   // Count: 2

drop(rc1);  // Count: 1, memory still alive
drop(rc2);  // Count: 0, memory freed
```

Drop ensures memory is freed only when the last owner is dropped.

