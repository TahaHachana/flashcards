## Role of rustc

What is `rustc` and how does it fit into the toolchain?

---

`rustc` is the Rust compiler.
It parses, type-checks, borrow-checks, and generates optimized machine code via LLVM.
It’s typically called by Cargo but can be run directly:

```bash
rustc main.rs
```

