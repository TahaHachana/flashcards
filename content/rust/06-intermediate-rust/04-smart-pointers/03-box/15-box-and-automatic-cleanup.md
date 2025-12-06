## Box and Automatic Cleanup

Explain how `Box` automatically cleans up heap memory. What happens when Box goes out of scope?

---

`Box` implements the `Drop` trait, which automatically frees heap memory when the Box goes out of scope.

**Automatic cleanup:**
```rust
fn main() {
    {
        let boxed = Box::new(String::from("Hello"));
        println!("{}", boxed);
    }  // boxed dropped here, heap memory freed automatically
    
    // boxed no longer accessible
}
```

**What happens:**
1. `boxed` goes out of scope (closing `}`)
2. `Drop::drop()` is called on `boxed`
3. Heap memory is deallocated
4. No memory leaks!

**Manual drop:**
```rust
let boxed = Box::new(String::from("Hello"));

// Explicitly drop early
drop(boxed);

// println!("{}", boxed);  // Error! Already dropped
```

**Key insight:** You never need to manually free `Box` memory - Rust's ownership system guarantees cleanup.

