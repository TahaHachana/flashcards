## Binary Size Trade-off

How do static and dynamic dispatch differ in their impact on binary size?

---

**Static dispatch (monomorphization)**:
- Generates specialized code for each type
- Larger binary size
- Can significantly increase with many types

**Dynamic dispatch (trait objects)**:
- One function handles all types
- Smaller binary size
- No duplication of code

**Example**:
```rust
// Large generic function
fn complex_process<T: Trait>(value: T) {
    // 500 lines of code
}

// Used with 10 types = 5000 lines in binary
// Used with 100 types = 50,000 lines in binary

// Trait object version = 500 lines regardless of types
fn complex_process(value: &dyn Trait) {
    // 500 lines of code
}
```

**Matters for**: Embedded systems, WASM, download size optimization.

