## External Dependencies as Crates

When you add a dependency in `Cargo.toml`, what exactly are you adding, and how do you access it?

---

**What you're adding:** Another crate (not a package or module)

```toml
[dependencies]
rand = "0.8"  # Adding the rand CRATE
```

**How to access:**
```rust
use rand::Rng;  // Use the crate name
```

**Key points:**
- Each dependency is its own crate with its own module tree
- You access dependencies using their crate name
- Cargo downloads and manages these external crates
- Each external crate was someone else's package that you're now using

