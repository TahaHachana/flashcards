# Reference Definition

What is a reference in Rust and how do you write immutable and mutable references?

---

A reference lets you borrow data without taking ownership.  
- Immutable reference: `&T`  
- Mutable reference: `&mut T`  

```rust
fn calculate_length(s: &String) -> usize {
    s.len()
}

fn change(s: &mut String) {
    s.push_str(", world");
}
```