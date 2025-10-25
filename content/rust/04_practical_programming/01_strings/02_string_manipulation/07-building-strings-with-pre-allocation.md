## Building Strings with Pre-allocation

Why should you pre-allocate capacity when building strings in loops? Show an example.

---

Pre-allocation avoids multiple reallocations:
```rust
// May reallocate multiple times
let mut result = String::new();
for i in 0..5 {
    result.push_str(&i.to_string());
}

// Single allocation
let mut result = String::with_capacity(100);
for i in 0..5 {
    result.push_str(&i.to_string());
}
```
The second version is more efficient because memory is allocated once upfront.

