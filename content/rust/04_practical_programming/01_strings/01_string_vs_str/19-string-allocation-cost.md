## String Allocation Cost

What is the performance cost of creating a String and when does this matter most?

---

Creating a String requires heap allocation:
```rust
let s = String::from("hello");  // Heap allocation
```
This matters most when creating many short-lived Strings in a loop, as each allocation has overhead. Consider using &str, string reuse, or pre-allocation with String::with_capacity() to minimize allocations.

