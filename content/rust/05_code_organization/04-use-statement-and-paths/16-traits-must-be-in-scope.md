## Traits Must Be In Scope

Why must traits be imported with `use` to call their methods?

---

**Rule**: To use a trait's methods, the trait must be in scope.

**Example of error**:
```rust
use std::fs::File;
// use std::io::Read;  // Forgot to import Read trait!

let mut file = File::open("data.txt")?;
let mut contents = String::new();
file.read_to_string(&mut contents)?;  // ERROR: method not found
```

**Fix**: Import the trait
```rust
use std::fs::File;
use std::io::Read;  // Import the trait

let mut file = File::open("data.txt")?;
file.read_to_string(&mut contents)?;  // Works!
```

**Why this matters**:
- Traits define methods that can be called on types
- Rust needs to know which trait provides a method
- Without the trait in scope, Rust can't find the method

**Common with**: `std::io::Read`, `std::io::Write`, `std::fmt::Display`

