## Enum Repr Attribute

What does `#[repr(u8)]` on an enum do?

---

It fixes the enum’s underlying representation for FFI or layout control:

```rust
#[repr(u8)]
enum Status {
    Ok = 0,
    NotFound = 1,
}
```

