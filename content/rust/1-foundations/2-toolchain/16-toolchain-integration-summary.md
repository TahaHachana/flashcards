## Toolchain Integration Summary

How do `rustup`, `rustc`, and `cargo` work together as an integrated toolchain?

---

* **`rustup`** manages installation, updates, and configuration of toolchains.
* **`cargo`** handles builds, tests, and dependency management.
* **`cargo`** internally invokes **`rustc`** to compile code using the toolchain managed by `rustup`.

This integration creates a unified, consistent Rust developer experience.

