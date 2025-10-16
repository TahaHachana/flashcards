## Workaround Documentation

How should you document workarounds or temporary solutions?

---

Clearly mark them with explanation and removal conditions.

```rust
// Workaround for bug #1234 in external API
// Remove once they fix in version 2.0
if status == 500 { retry(); }
```

