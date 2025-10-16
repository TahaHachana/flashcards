## Documenting Enums

How do you document enums and their variants?

---

Use /// before the enum and before each variant.

```rust
/// Connection states
enum ConnectionState {
    /// Not connected
    Disconnected,
    /// Connection active
    Connected,
}
```

