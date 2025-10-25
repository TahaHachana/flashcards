## Slice Memory Layout

What does a slice contain internally?

---

A "fat pointer" with two components: pointer to first element and length. Size: two usize values (16 bytes on 64-bit systems).

```rust
// Internally: ptr + len
let slice = &arr[1..4];
```

