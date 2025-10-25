## Trimming Whitespace

What are the three trim methods and what does each do?

---

```rust
let s = "  hello world  ";
s.trim();        // "hello world" - removes both ends
s.trim_start();  // "hello world  " - removes left
s.trim_end();    // "  hello world" - removes right
```
All return new &str, original unchanged. Remove whitespace from the specified ends.

