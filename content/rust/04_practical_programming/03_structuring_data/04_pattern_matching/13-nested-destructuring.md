## Nested Destructuring

How do you destructure nested enums and structs in a single pattern?

---

Patterns can be arbitrarily nested:

```rust
enum Color {
    Rgb(i32, i32, i32),
    Hsv(i32, i32, i32),
}

enum Message {
    ChangeColor(Color),
}

let msg = Message::ChangeColor(Color::Hsv(0, 160, 255));

match msg {
    Message::ChangeColor(Color::Rgb(r, g, b)) => {
        println!("RGB({}, {}, {})", r, g, b)
    }
    Message::ChangeColor(Color::Hsv(h, s, v)) => {
        println!("HSV({}, {}, {})", h, s, v)
    }
    _ => {}
}
```

The pattern structure mirrors the data structure exactly. You can nest as deeply as needed to extract the data you want.

