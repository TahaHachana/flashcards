## Exhaustive Matching Requirement

What happens if you don't handle all enum variants in a match expression?

---

**Compile error** - Rust requires exhaustive matching:

```rust
enum Message {
    Quit,
    Move { x: i32, y: i32 },
    Write(String),
}

fn process(msg: Message) {
    match msg {
        Message::Quit => println!("Quit"),
        Message::Write(text) => println!("{}", text),
        // ERROR: non-exhaustive patterns: `Move { .. }` not covered
    }
}
```

**Solutions**:

1. Handle all variants explicitly:
```rust
match msg {
    Message::Quit => {},
    Message::Move { x, y } => {},
    Message::Write(text) => {},
}
```

2. Use catch-all pattern:
```rust
match msg {
    Message::Quit => {},
    _ => {}  // Handles remaining variants
}
```

This prevents forgetting to handle cases when you add new variants.

