## Returning Results

How can you return a `Result` from a function and propagate errors?

---

Use `Result<T, E>` as the return type, and the `?` operator to propagate errors.

Example:

```rust
use std::fs::File;
use std::io;

fn try_open() -> io::Result<File> {
    File::open("Cargo.toml")
}
```
