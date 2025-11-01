## What Are Paths in Rust?

What is a path in Rust, and why do we need paths?

---

**A path** is a way to name an item in Rust's module tree.

**Like navigation systems**:
- File system: `/home/user/documents/file.txt`
- Rust module: `std::collections::HashMap`

**Why we need them**:
- Navigate the module tree to reference items
- Specify exactly which item we want
- Avoid ambiguity when items have similar names

**Example**:
```rust
std::collections::HashMap::new();
crate::database::Connection::connect();
```

Paths tell Rust exactly where to find an item in the module tree.

