## Integer Literals

What forms can integer literals take in Rust?

---

* Decimal: `98_222`
* Hex: `0xff`
* Octal: `0o77`
* Binary: `0b1111_0000`
* Byte (u8 only): `b'A'`

Underscores `_` can be used as visual separators.
Literals can also have type suffixes:

```rust
let x = 42u8;
let y = 3.14f32;
```

