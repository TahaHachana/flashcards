## Accessing Enum Variant Data

Why can't you directly access data in enum variants, and what's the correct way to do it?

---

**Can't use direct access**:
```rust
enum Message {
    Write(String),
}

let msg = Message::Write(String::from("hello"));
// println!("{}", msg.0);  // ERROR: can't index into enum
```

**Must use pattern matching**:
```rust
match msg {
    Message::Write(text) => println!("{}", text),
    _ => {}
}

// Or if let
if let Message::Write(text) = msg {
    println!("{}", text);
}
```

**Why**: The enum could be any variant. You must prove which variant it is through pattern matching before accessing its data. This ensures type safety.

