## Pattern Matching Best Practices

What are five best practices for using pattern matching in Rust?

---

1. **Put specific patterns before general ones**
```rust
match x {
    5 => {},      // Specific first
    _ => {},      // General last
}
```

2. **Use if let for single patterns**
```rust
// Clearer than match with _ => {}
if let Some(value) = option {
    // use value
}
```

3. **Use references to avoid moving**
```rust
match &opt {
    Some(s) => {},  // s is &String, opt not moved
    None => {},
}
```

4. **Leverage exhaustiveness checking**
```rust
// Compiler ensures all variants handled
match msg {
    Message::Quit => {},
    Message::Move { .. } => {},
    Message::Write(_) => {},
}
```

5. **Use match guards for complex conditions**
```rust
match num {
    x if x < 0 => println!("negative"),
    x if x > 100 => println!("large"),
    x => println!("{}", x),
}
```

Pattern matching is safer than chains of if/else and catches logic errors at compile time.

