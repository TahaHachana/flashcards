## Default Immutability

What is the default mutability of variables in Rust, and why?

---

By default, variables in Rust are **immutable** to encourage safety, thread safety, and easier reasoning about code.  
Even if the original binding is immutable, you can still reuse the name later via **shadowing**.  
```rust
fn main() {
    let x = 5;
    println!("x = {x}");
    // x = 6; // ❌ compile-time error
}
```

