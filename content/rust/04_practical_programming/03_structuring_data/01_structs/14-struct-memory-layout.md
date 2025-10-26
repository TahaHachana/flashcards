## Struct Memory Layout

How are struct fields laid out in memory in Rust?

---

- **Classic structs**: Fields stored in memory in declaration order (with potential padding for alignment)
- **Tuple structs**: Similar to classic structs but without names
- **Unit structs**: Zero-sized types (ZSTs) - take up **no memory**

The compiler may reorder fields to optimize memory layout (minimize padding) unless you use `#[repr(C)]` to enforce C-compatible layout.

Example: A struct with `u8`, `u64`, `u8` might be reordered to reduce padding from alignment requirements.

