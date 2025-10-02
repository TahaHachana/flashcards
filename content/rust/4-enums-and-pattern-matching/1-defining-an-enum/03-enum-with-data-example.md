## Enum With Data Example

Show an enum where each variant carries different kinds of data.

---

```rust
enum Message {
    Quit,                         // no data
    Move { x: i32, y: i32 },      // struct-like
    Write(String),                // tuple-like
    ChangeColor(i32, i32, i32),   // multiple values
}
```

