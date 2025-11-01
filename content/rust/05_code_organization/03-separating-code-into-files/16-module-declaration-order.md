## Module Declaration Order Matters

Does the order of module declarations matter, and why?

---

**Yes**, for `use` statements - modules must be declared before you can import from them.

**Correct order**:
```rust
mod database;           // Declare first
use database::connect;  // Then import

fn main() {
    connect();
}
```

**Wrong order**:
```rust
use database::connect;  // ERROR - database not yet declared
mod database;           // Too late!
```

**Among module declarations**: Order generally doesn't matter
```rust
mod database;
mod api;      // Both work fine in any order
mod models;
```

**Best practice**: Declare all modules at the top of the file, before any `use` statements.

