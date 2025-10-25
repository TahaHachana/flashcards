## String Capacity vs Length

What's the difference between a String's length and capacity? Show an example.

---

Length is bytes currently used, capacity is bytes allocated:
```rust
let mut s = String::with_capacity(10);
println!("{}, {}", s.len(), s.capacity());
// Length: 0, Capacity: 10

s.push_str("hello");
println!("{}, {}", s.len(), s.capacity());
// Length: 5, Capacity: 10 (no reallocation needed)
```
Capacity ≥ length. Extra capacity allows growth without reallocation.

