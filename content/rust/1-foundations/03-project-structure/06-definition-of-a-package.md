## Definition of a Package

What is a package in Rust, and how does it relate to crates?

---

A **package** is a collection of one or more crates managed by a single `Cargo.toml`.
Every package must contain at least one crate (binary or library).
Example: a package with a library crate and one binary crate.

```
src/lib.rs
src/main.rs
```

