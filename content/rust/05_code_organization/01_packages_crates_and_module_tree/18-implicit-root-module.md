## Implicit Root Module

What is the implicit root module in a Rust crate, and why don't you declare it?

---

**Implicit root:**
- For `src/lib.rs`: The file itself is the library crate's root module
- For `src/main.rs`: The file itself is the binary crate's root module

**Why it's implicit:**
- You don't write `mod crate` anywhere
- These files automatically become the root of the module tree
- All other modules are descendants of this root

**Example:**
```rust
// src/lib.rs - This IS the root module
mod utils;  // Child module
mod database;  // Child module
```

