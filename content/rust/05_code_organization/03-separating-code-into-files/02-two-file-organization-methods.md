## Two Ways to Organize Module Files

What are the two conventions for organizing multi-file modules in Rust?

---

**Method 1: Filename matches module name**
```
src/network.rs
```
```rust
// In src/lib.rs
mod network;  // Looks for src/network.rs
```

**Method 2: Directory with mod.rs**
```
src/network/mod.rs
```
```rust
// In src/lib.rs
mod network;  // Looks for src/network/mod.rs
```

**Both are valid**, and for `mod network;`, Rust will check for both locations. Method 1 is simpler; Method 2 is used when a module has submodules.

