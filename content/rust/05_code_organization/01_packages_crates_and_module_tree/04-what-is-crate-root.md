## What Is a Crate Root?

What is a crate root, and what are the conventional crate root files in Rust?

---

The **crate root** is the source file that the Rust compiler starts from and makes up the root module of your crate.

**Conventional roots:**
- `src/main.rs` - Root of the binary crate
- `src/lib.rs` - Root of the library crate

These files form the implicit root module of their respective crates (you don't write `mod crate`, it's implicit).

