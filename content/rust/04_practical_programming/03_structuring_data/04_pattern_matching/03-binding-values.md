## Binding Values in Patterns

How do you extract and bind data from enum variants in a match expression?

---

Use pattern syntax to destructure variants and bind values:

```rust
enum Message {
    Quit,
    Move { x: i32, y: i32 },
    Write(String),
    ChangeColor(u8, u8, u8),
}

match msg {
    Message::Quit => println!("Quit"),
    
    Message::Move { x, y } => {  // Extract named fields
        println!("Moving to ({}, {})", x, y);
    }
    
    Message::Write(text) => {  // Extract tuple data
        println!("Text: {}", text);
    }
    
    Message::ChangeColor(r, g, b) => {  // Extract multiple values
        println!("RGB({}, {}, {})", r, g, b);
    }
}
```

The pattern syntax mirrors the variant's structure.

