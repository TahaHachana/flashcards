## Cross-Compilation

What is cross-compilation and does Rust support it?

---

Cross-compilation means compiling on one platform for another. Rust supports this well - you can compile on Linux for Windows, or macOS for Linux, without running on the target platform.

```bash
cargo build --target x86_64-pc-windows-gnu
```

