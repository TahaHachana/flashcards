## Multiple Patterns with Pipe

How do you match multiple patterns in a single arm using the pipe operator?

---

Use `|` to match multiple patterns in one arm:

```rust
let x = 1;

match x {
    1 | 2 => println!("one or two"),
    3 | 4 | 5 => println!("three through five"),
    _ => println!("something else"),
}

// Works with more complex patterns too
match msg {
    Message::Quit | Message::Exit => println!("shutting down"),
    Message::Write(text) => println!("{}", text),
}
```

The `|` means "or" - if any pattern matches, that arm executes. All patterns in the arm must bind the same variables.

