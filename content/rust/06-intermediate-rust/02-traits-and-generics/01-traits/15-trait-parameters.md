## Trait-Based Function Parameters

Show two ways to write a function that accepts any type implementing the `Display` trait.

---

1. **Generic with trait bound**:
```rust
fn print<T: Display>(item: T) {
    println!("{}", item);
}
```

2. **impl Trait syntax**:
```rust
fn print(item: impl Display) {
    println!("{}", item);
}
```

Both mean the same thing: the function accepts any type `T` that implements `Display`.

