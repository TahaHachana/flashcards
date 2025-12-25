## Hidden Lines Common Patterns

What are common patterns for using hidden lines in doc tests?

---

1. Hiding imports:
```rust
/// ```
/// # use my_crate::Config;
/// let config = Config::default();
/// ```
```

2. Hiding error handling:
```rust
/// ```
/// # fn main() -> Result<(), Box<dyn std::error::Error>> {
/// let content = read_file("data.txt")?;
/// # Ok(())
/// # }
/// ```
```

3. Hiding setup:
```rust
/// ```
/// # let mut game = Game::new();
/// # game.start();
/// # game.advance_to_level(5);
/// // User sees this:
/// game.save_checkpoint();
/// ```
```

4. Hiding cleanup:
```rust
/// ```
/// # std::fs::write("test.txt", "data").unwrap();
/// let content = read_file("test.txt");
/// # std::fs::remove_file("test.txt").unwrap();
/// ```
```

Hide boilerplate, show essence.

