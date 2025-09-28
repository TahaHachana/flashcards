## Documentation Checklist

What should you check before committing code regarding Rust documentation?

---

* Every public item has a one-line summary.
* At least one example compiles with `cargo test`.
* Panic conditions documented.
* Errors explained for `Result` types.
* Safety invariants for `unsafe` functions.
* Intra-doc links resolve correctly.
* Lines kept under ~100 chars.
* Crate/module-level docs provide clear overview.
* Comments explain *why*, not just *what*.

