## Capacity Method

What does the capacity() method tell you and how does it differ from len()?

---

```rust
let mut s = String::with_capacity(10);
s.push_str("hi");
println!("len: {}, capacity: {}", s.len(), s.capacity());
// len: 2, capacity: 10
```
len() returns bytes currently used in the string. capacity() returns total bytes allocated. Capacity is always ≥ length. Extra capacity allows growth without reallocation.

