## Cargo New Command Creates What?

When you run `cargo new my_project`, what exactly does Cargo create?

---

Cargo creates a **package** that contains one **binary crate**.

```
my_project/           ← Package
├── Cargo.toml        ← Package manifest
└── src/
    └── main.rs       ← Binary crate root
```

**What you get:**
- A package named "my_project"
- One binary crate with root at `src/main.rs`
- An implicit root module in `main.rs`
- A `Cargo.toml` file for configuration

**To create a library instead:** `cargo new --lib my_project`

