## Cargo.toml Structure and Purpose

What information goes in a `Cargo.toml` file, and what is its purpose?

---

`Cargo.toml` is the **package manifest** that describes how to build the crates in a package.

**Key sections:**
```toml
[package]
name = "my_project"
version = "0.1.0"
edition = "2021"

[dependencies]
rand = "0.8"
serde = "1.0"
```

**Purpose:**
- Define package metadata (name, version, edition)
- Manage dependencies (external crates)
- Configure build settings
- Specify multiple binaries (optional)

