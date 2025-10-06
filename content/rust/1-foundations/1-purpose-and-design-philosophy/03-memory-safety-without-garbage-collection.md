## Memory Safety Without Garbage Collection

How does Rust guarantee memory safety without using a garbage collector?

---

Rust’s **ownership model** defines who owns each value,  
the **borrow checker** ensures valid references,  
and memory is freed deterministically when ownership goes out of scope.  

```rust
fn main() {
    let s = String::from("hi");
    let t = s;         // ownership moves to t
    // println!("{}", s); // ❌ compile-time error
    println!("{}", t);  // ✅ safe
}
```

