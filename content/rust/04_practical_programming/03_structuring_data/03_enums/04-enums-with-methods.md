## Enums with Methods

Can enums have methods like structs? Show an example with both associated functions and instance methods.

---

**Yes**, enums can have methods in impl blocks:

```rust
enum Message {
    Quit,
    Write(String),
}

impl Message {
    // Associated function (constructor)
    fn new_write(text: &str) -> Self {
        Message::Write(String::from(text))
    }
    
    // Instance method
    fn call(&self) {
        match self {
            Message::Quit => println!("Quitting"),
            Message::Write(text) => println!("Writing: {}", text),
        }
    }
    
    // Method checking variant type
    fn is_quit(&self) -> bool {
        matches!(self, Message::Quit)
    }
}

// Usage
let msg = Message::new_write("hello");
msg.call();
```

Methods work identically to struct methods.

