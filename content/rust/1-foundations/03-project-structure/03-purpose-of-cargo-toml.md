## Purpose of Cargo.toml

What information is stored in `Cargo.toml`, and why is it important?

---

`Cargo.toml` is the **manifest file** defining:
- Package metadata (`name`, `version`, `edition`).  
- Dependencies from crates.io or local paths.  
- Optional `[dev-dependencies]` for tests and `[features]` for configuration.  
It tells Cargo how to build and link your project.

