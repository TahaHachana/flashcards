## Old vs Modern Module File Organization

What's the difference between old-style `mod.rs` and modern Rust 2018+ module organization?

---

**Old style** (before Rust 2018):
```
src/
├── lib.rs
└── network/
    ├── mod.rs         ← Module contents here
    ├── server.rs
    └── client.rs
```

**Modern style** (Rust 2018+):
```
src/
├── lib.rs
├── network.rs         ← Module contents here
└── network/
    ├── server.rs
    └── client.rs
```

**Both work**, but modern style advantages:
- No special `mod.rs` files
- `network.rs` is at same level as `network/` directory
- More intuitive structure
- Less confusion (every `mod.rs` looked the same)

**Migration**: Can adopt gradually, both styles can coexist.

