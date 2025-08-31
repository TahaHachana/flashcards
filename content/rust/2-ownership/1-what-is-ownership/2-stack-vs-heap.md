# Stack vs Heap

How do stack and heap allocation differ in Rust?

---

- The stack holds fixed-size values and follows LIFO (fast).  
- The heap holds dynamically sized data (slower due to allocation).  

```rust
// Stack: size known at compile time
let x: i32 = 42;

// Heap: dynamic String allocation
let s: String = String::from("hello, heap");
```