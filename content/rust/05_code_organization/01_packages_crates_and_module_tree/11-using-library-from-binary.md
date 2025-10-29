## Using Library from Binary in Same Package

If a package contains both `src/lib.rs` and `src/main.rs`, how does the binary crate use the library crate?

---

The binary must explicitly import the library using the package name:

```rust
// Assuming package name is "my_project" in Cargo.toml
// In src/main.rs:
use my_project::some_function;

fn main() {
    some_function();
}
```

**Key point:** `main.rs` and `lib.rs` don't automatically share code—you must use the package name to import from the library.

