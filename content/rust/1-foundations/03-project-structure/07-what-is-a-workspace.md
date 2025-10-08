## What Is a Workspace

What is a Cargo workspace, and what are its advantages?

---

A **workspace** is a collection of related packages that share:

* One `Cargo.lock` for dependency resolution.
* One `target/` directory for builds.

Advantages:

* Unified builds (`cargo build` applies to all members).
* Consistent dependency versions.
* Simplified cross-crate development.

