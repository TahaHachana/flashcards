## Code Bloat Problem

What is code bloat with generics, and when does it become a problem?

---

**Code bloat** occurs when monomorphization generates many copies of the same function for different types, increasing binary size.

```rust
fn process<T: Display>(value: T) {
    println!("Processing: {}", value);
    // ... 100 more lines of code ...
}

fn main() {
    process(1);           // +100 lines for i32
    process(2.5);         // +100 lines for f64
    process("text");      // +100 lines for &str
    process(String::new()); // +100 lines for String
    // Binary contains 400+ lines of nearly identical code
}
```

**When it matters**: Large generic functions used with many types, embedded systems, or WASM where size is critical.

**Solution**: Use trait objects for size-critical code.

