## Debug vs Display Trait Bounds

What's the difference between `Debug` and `Display` trait bounds, and how do you know which to use?

---

**Debug** (`{:?}`): For programmer-facing output, debugging
**Display** (`{}`): For user-facing output, formatted display

```rust
fn debug_print<T: Debug>(value: T) {
    println!("{:?}", value);  // Uses Debug
}

fn display_print<T: Display>(value: T) {
    println!("{}", value);    // Uses Display
}
```

**Rule**: If you're using `{:?}`, you need `Debug`. If you're using `{}`, you need `Display`.

Most types implement `Debug` (often via `#[derive(Debug)]`), but fewer implement `Display`.

