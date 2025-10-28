## Question Mark Vs Manual Propagation

Compare code with and without the `?` operator for error propagation.

---

**Without `?` (verbose):**
```rust
fn read_file() -> Result<String, io::Error> {
    let mut file = match File::open("file.txt") {
        Ok(f) => f,
        Err(e) => return Err(e),
    };
    let mut contents = String::new();
    match file.read_to_string(&mut contents) {
        Ok(_) => Ok(contents),
        Err(e) => Err(e),
    }
}
```

**With `?` (clean):**
```rust
fn read_file() -> Result<String, io::Error> {
    let mut file = File::open("file.txt")?;
    let mut contents = String::new();
    file.read_to_string(&mut contents)?;
    Ok(contents)
}
```

Both compile to the same code - `?` is zero-cost abstraction.

