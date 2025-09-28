## Documentation Quality Gates

What compiler and tool options help enforce documentation quality in Rust?

---

* `#![deny(missing_docs)]` → require docs for all public items.
* `#![warn(rustdoc::broken_intra_doc_links)]` → warn on broken links.
* `cargo doc` → preview generated docs.
* `cargo test` → validate examples in docs.

