## Chaining Plus Operators

What happens to s1, s2, and s3 in this code?
```rust
let s1 = String::from("tic");
let s2 = String::from("tac");
let s3 = String::from("toe");
let s = s1 + "-" + &s2 + "-" + &s3;
```

---

s1 is moved (no longer valid), while s2 and s3 are borrowed (still valid). The first + moves s1, subsequent + operators borrow the remaining strings. This gets awkward with many strings since ownership of the first is lost.

