## Extract and Transform Pattern

How do you extract part of a string and transform it?

---

```rust
let s = String::from("hello world");
let first = &s[0..5];           // Extract: "hello"
let upper = first.to_uppercase(); // Transform: "HELLO"
```
First slice to extract the desired part (creates &str), then apply transformation methods which typically return new Strings.

