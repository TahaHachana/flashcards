## Question Mark In Main

Can you use the `?` operator in `main()` and if so, how?

---

Yes! Since Rust 1.26, `main()` can return `Result`:

```rust
// Modern style - main returns Result
fn main() -> Result<(), Box<dyn std::error::Error>> {
    let config = load_config("config.txt")?;
    process(config)?;
    Ok(())
}
```

If `main` returns an `Err`, the program exits with a non-zero status code and prints the error. This enables using `?` throughout your application, including in `main`.

