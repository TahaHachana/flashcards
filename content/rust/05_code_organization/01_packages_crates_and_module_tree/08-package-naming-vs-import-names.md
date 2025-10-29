## Package Naming vs Import Names

If a package is named `my-awesome-lib` in `Cargo.toml`, how do you import it in Rust code?

---

```rust
// Cargo.toml
[package]
name = "my-awesome-lib"  // Hyphens allowed

// In code:
use my_awesome_lib::something;  // Hyphens become underscores!
```

**Rule:** Hyphens in package names are converted to underscores in import paths and code.

