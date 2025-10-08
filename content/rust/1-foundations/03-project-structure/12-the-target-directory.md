## The Target Directory

What is the purpose of the `target` directory in a Rust project?

---

`target/` stores compiled artifacts, build caches, and test outputs.
It contains `debug/` and `release/` builds.
Clean it with:

```bash
cargo clean
```

Build optimized binaries with:

```bash
cargo build --release
```

