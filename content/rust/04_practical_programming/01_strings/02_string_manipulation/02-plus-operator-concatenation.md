## Plus Operator Concatenation

What happens to s1 and s2 in this code?
```rust
let s1 = String::from("Hello, ");
let s2 = String::from("world!");
let s3 = s1 + &s2;
```

---

s1 is moved (ownership transferred, no longer valid), while s2 is borrowed (still valid). The + operator takes ownership of the left operand and borrows the right operand, returning a new String. This is why you can't use s1 afterwards but can still use s2.

