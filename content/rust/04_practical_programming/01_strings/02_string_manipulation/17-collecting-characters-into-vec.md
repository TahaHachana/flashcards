## Collecting Characters into Vec

How do you convert a String into a vector of characters?

---

```rust
let s = String::from("hello");
let chars: Vec<char> = s.chars().collect();
// chars: ['h', 'e', 'l', 'l', 'o']
```
Use chars() to create an iterator over characters, then collect() to gather them into a Vec<char>.

