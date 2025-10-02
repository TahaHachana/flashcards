## Match Exhaustiveness

What rule does Rust enforce for `match` expressions?

---

All possible cases must be covered. If some values are unhandled, the compiler reports an error.
A `_` wildcard can act as a catch-all:

```rust
match coin {
    Coin::Penny => 1,
    Coin::Nickel => 5,
    _ => 0,
}
```

