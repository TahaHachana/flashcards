## Fast Byte Operations

Which string operations are O(1) constant time?

---

```rust
s.len()      // O(1) - just returns length field
s.is_empty() // O(1) - checks if length is 0
&s[0..10]    // O(1) - if boundaries are valid
```
Byte-level operations are constant time because they don't require scanning or validation - they work directly with the byte array.

