## How String Uses Deref and Drop

Explain how `String` implements both `Deref` and `Drop` traits.

---

**Deref implementation:**
```rust
impl Deref for String {
    type Target = str;
    
    fn deref(&self) -> &str {
        // Returns &str slice of the string data
    }
}
```

**Enables:** Using `String` where `&str` is expected
```rust
fn takes_str(s: &str) { }

let s = String::from("hello");
takes_str(&s);      // &String -> &str via Deref
println!("{}", s.len());  // Can call str methods
```

**Drop implementation:**
```rust
impl Drop for String {
    fn drop(&mut self) {
        // Deallocates heap buffer
    }
}
```

**Enables:** Automatic memory management
```rust
{
    let s = String::from("hello");
    // Use s
}  // Heap buffer automatically freed
```

This is why String is easy to use but doesn't leak memory - Deref makes it ergonomic, Drop makes it safe.

