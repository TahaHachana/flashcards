## Adding Cross-Compilation Targets

How can you add a new compilation target, such as WebAssembly, using `rustup`?

---

Use the `rustup target add` command:

```bash
rustup target add wasm32-unknown-unknown
```

This enables building binaries for the WebAssembly platform or other architectures.

