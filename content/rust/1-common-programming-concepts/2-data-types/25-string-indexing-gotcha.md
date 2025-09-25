## String Indexing Gotcha

Why can’t you index into a Rust `String` with `s[0]`?

---

Rust `String` is UTF-8 encoded; characters may use multiple bytes.
Direct indexing is ambiguous and not allowed.

Example:

```rust
let s = String::from("hello");
// println!("{}", s[0]); // error
println!("{}", &s[0..1]); // "h"
```

