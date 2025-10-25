## Character Position to Byte Position

How do you convert a character position to its corresponding byte position?

---

```rust
fn char_pos_to_byte_pos(s: &str, char_pos: usize) -> Option<usize> {
    s.char_indices().nth(char_pos).map(|(i, _)| i)
}

let s = String::from("你好世界");
let byte_pos = char_pos_to_byte_pos(&s, 2);
println!("{:?}", byte_pos);  // Some(6)
```
Use char_indices().nth(n) to get the byte index where the nth character starts.

