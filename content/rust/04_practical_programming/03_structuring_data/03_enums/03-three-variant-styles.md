## Three Variant Styles

What are the three styles of enum variants in Rust, and what struct type does each resemble?

---

1. **Unit variants** (no data) - like unit structs
```rust
enum Message {
    Quit,  // No associated data
}
```

2. **Tuple variants** - like tuple structs
```rust
enum Message {
    Write(String),              // One field
    ChangeColor(u8, u8, u8),   // Multiple fields
}
```

3. **Struct variants** - like classic structs
```rust
enum Message {
    Move { x: i32, y: i32 },  // Named fields
}
```

All three can coexist in the same enum, and each variant acts like its own constructor function.

