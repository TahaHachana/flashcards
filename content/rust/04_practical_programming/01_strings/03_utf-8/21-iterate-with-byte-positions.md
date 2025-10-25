## Iterate with Byte Positions

How do you iterate over characters while also getting their byte positions?

---

```rust
let s = String::from("Hello, 世界!");

for (byte_pos, ch) in s.char_indices() {
    println!("Character '{}' at byte {}", ch, byte_pos);
}
```
char_indices() gives you (byte_position, character) tuples, useful when you need to know where each character starts in the byte array.

