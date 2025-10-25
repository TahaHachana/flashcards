## String Methods Return New Data

Do most string methods modify the original string or return new data?

---

Most string methods return new String or &str without modifying the original:
```rust
let s = "hello";
let upper = s.to_uppercase();  // Returns new String
// s is still "hello"

let trimmed = s.trim();  // Returns new &str
// s is unchanged
```
Exception: mutable methods like push_str(), push(), clear() modify in place.

