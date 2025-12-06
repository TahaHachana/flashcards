## How Box Uses Deref and Drop

Explain how `Box<T>` implements both `Deref` and `Drop` traits, and what each enables.

---

**Deref implementation:**
```rust
impl<T> Deref for Box<T> {
    type Target = T;
    
    fn deref(&self) -> &T {
        // Returns reference to heap data
    }
}
```

**Enables:** Using `Box<T>` like `&T`
```rust
fn takes_i32(n: &i32) { }

let boxed = Box::new(5);
takes_i32(&boxed);  // &Box<i32> -> &i32 via Deref
```

**Drop implementation:**
```rust
impl<T> Drop for Box<T> {
    fn drop(&mut self) {
        // Deallocates heap memory
    }
}
```

**Enables:** Automatic cleanup
```rust
{
    let boxed = Box::new(5);
    // Use boxed
}  // Heap memory automatically freed via Drop
```

**Together:** Box acts like a reference but owns its data and cleans up automatically.

