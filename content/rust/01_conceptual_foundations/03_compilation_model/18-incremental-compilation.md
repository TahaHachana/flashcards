## Incremental Compilation

How does incremental compilation improve compile times?

---

It only recompiles changed code and its dependencies, caches compilation artifacts, and tracks dependencies at a fine-grained level. This dramatically speeds up rebuilds during development.

