## What Is a Rust Package?

What is a Rust package, and what are its key requirements and rules?

---

A package is a bundle of one or more crates managed by Cargo.

**Requirements:**
- Must contain a `Cargo.toml` file (package manifest)
- Must contain at least one crate (either library or binary)

**Rules:**
- Can contain at most ONE library crate
- Can contain ANY NUMBER of binary crates
- Created with `cargo new package_name`

