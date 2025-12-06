## Manual Drop with std::mem::drop

Why can't you call `.drop()` directly, and how do you drop a value early?

---

**Cannot call `.drop()` directly:**
```rust
let s = String::from("hello");
// s.drop();  // Error! Can't call drop explicitly
```

**Error reason:** Rust will still call `drop()` when `s` goes out of scope, which would cause a double-free.

**Solution: Use `std::mem::drop()`:**
```rust
fn main() {
    let s = String::from("hello");
    println!("Created: {}", s);
    
    drop(s);  // Explicitly drop s early
    
    // println!("{}", s);  // Error! s was moved into drop
}
```

**Why `std::mem::drop()` works:**
```rust
pub fn drop<T>(_x: T) { }
```

It takes ownership of the value and does nothing. When `drop()` returns, its parameter goes out of scope and is naturally dropped. This prevents double-drop because the value was moved.

