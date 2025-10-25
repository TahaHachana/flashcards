## Using char_indices for Position and Character

What does this code print and what information does char_indices() provide?
```rust
let s = String::from("你好世界");
for (index, ch) in s.char_indices() {
    println!("Byte {} starts character '{}'", index, ch);
}
```

---

```
Byte 0 starts character '你'
Byte 3 starts character '好'
Byte 6 starts character '世'
Byte 9 starts character '界'
```
char_indices() provides both the byte index where each character starts AND the character itself. Useful for finding valid slice positions.

