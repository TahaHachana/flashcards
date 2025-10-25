## Truncate Method

What does the truncate() method do and does it modify the string?

---

```rust
let mut s = String::from("hello world");
s.truncate(5);  // s is now "hello"
```
truncate() modifies the String in place, keeping only the first n bytes and discarding the rest. Requires a mutable String. Does not deallocate capacity.

