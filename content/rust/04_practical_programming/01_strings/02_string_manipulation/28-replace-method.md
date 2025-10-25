## Replace Method

How does the replace() method work and what does it return?

---

```rust
let s = "  hello world  ";
let new_s = s.replace("world", "Rust");
// new_s: "  hello Rust  "
// s is unchanged
```
replace() returns a new String with all occurrences of the pattern replaced. The original string is not modified.

