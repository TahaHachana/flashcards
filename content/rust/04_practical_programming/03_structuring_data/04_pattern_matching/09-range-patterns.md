## Range Patterns

How do range patterns work in Rust and what types support them?

---

Use `..=` for inclusive ranges in patterns:

```rust
let x = 5;

match x {
    1..=5 => println!("one through five"),
    6..=10 => println!("six through ten"),
    _ => println!("something else"),
}

// Works with chars
let c = 'c';

match c {
    'a'..='j' => println!("early letter"),
    'k'..='z' => println!("late letter"),
    _ => println!("something else"),
}
```

**Supported types**: 
- Numeric types (integers, floats)
- `char`

**Not supported**: Strings, custom types (without special implementations)

Ranges are inclusive on both ends with `..=`.

