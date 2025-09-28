## Module and Crate Docs

How do you write module-level and crate-level documentation in Rust?

---

Use `//!` at the top of a file or module:

* For modules, describe provided items and usage.
* For crates, give a summary, overview, usage examples, and list of modules.

```rust
//! # My Crate
//!
//! Provides utilities for X.
//!
//! ## Modules
//! - [`mod_a`] — A feature
//! - [`mod_b`] — Another feature
```

