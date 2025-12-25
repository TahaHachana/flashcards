## Standard Binary Testing Pattern

What is the standard pattern for making binary projects testable?

---

Split logic between `lib.rs` and thin `main.rs`:

**src/lib.rs** (all logic):
```rust
pub fn process_data(input: &str) -> Result<String, String> {
    Ok(format!("Processed: {}", input))
}

pub fn run() -> Result<(), String> {
    let result = process_data("example")?;
    println!("{}", result);
    Ok(())
}
```

**src/main.rs** (thin wrapper):
```rust
use my_project;

fn main() {
    if let Err(e) = my_project::run() {
        eprintln!("Error: {}", e);
        std::process::exit(1);
    }
}
```

Now integration tests can import and test `my_project::process_data()` and `my_project::run()`.

