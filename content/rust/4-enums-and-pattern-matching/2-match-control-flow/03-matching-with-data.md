## Matching With Data

How can a `match` destructure enum variants with data?

---

By binding data inside the pattern:

```rust
enum Coin {
    Penny,
    Nickel,
    Quarter(String),
}

match coin {
    Coin::Quarter(state) => println!("Quarter from {state}!"),
    _ => println!("Other coin"),
}
```

