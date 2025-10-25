## Visualizing UTF-8 Storage

How is "café" stored in memory as UTF-8 bytes?

---

```rust
let s = String::from("café");
// Memory: [0x63, 0x61, 0x66, 0xC3, 0xA9]
//          'c'   'a'   'f'   'é' (2 bytes)
```
The string has 4 characters but 5 bytes because 'é' requires 2 bytes (0xC3 0xA9). This shows why byte position ≠ character position.

