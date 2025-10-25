## &str Immutability

Can you have a mutable &str reference? Why or why not?

---

No, &str is always immutable. There's no &mut str in practice. You cannot modify data through a &str:
```rust
let slice: &str = &s;
slice.push_str(" world");  // Error: &str is immutable
```
For mutable string operations, you need a String or &mut String.

