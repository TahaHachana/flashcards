## At Bindings (@)

What are @ bindings and why would you use them?

---

`@` lets you **bind a value while also testing it**:

```rust
enum Message {
    Hello { id: i32 },
}

let msg = Message::Hello { id: 5 };

match msg {
    Message::Hello {
        id: id_var @ 3..=7,  // Bind AND test range
    } => println!("Found id {} in range", id_var),
    
    Message::Hello { id: 10..=12 } => {
        println!("In another range")
        // Can't use the actual value here!
    }
    
    Message::Hello { id } => println!("Other id: {}", id),
}
```

**Without @**: You can test a range but can't access the value
**With @**: You can test a range AND bind the value to use it

Syntax: `variable @ pattern`

