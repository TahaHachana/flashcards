## Match Expression Basics

What are the four key properties of match expressions in Rust?

---

1. **Exhaustive**: Must handle all possible values (compiler enforced)

2. **Returns a value**: All arms must return the same type
```rust
let result = match x {
    1 => "one",
    2 => "two",
    _ => "other",
};
```

3. **First match wins**: Patterns checked top-to-bottom
```rust
match x {
    _ => println!("anything"),  // Would match everything
    5 => println!("five"),      // Never reached - unreachable!
}
```

4. **No fall-through**: Unlike switch in other languages, only the matched arm executes

Use `_` as a catch-all pattern for unhandled cases.

