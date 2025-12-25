## Binary vs Library Testing Problem

Why can't binary crates (with only `src/main.rs`) be tested directly by integration tests?

---

Binary crates cannot be integration tested because:
- They don't export any items (no public interface)
- They're meant to be run, not imported
- Integration tests cannot import them

Example:
```rust
// src/main.rs (binary only)
fn main() {
    println!("Hello");
}

fn helper() -> i32 { 42 }  // Can't be made public
```

```rust
// tests/test.rs
use my_binary;  // ❌ ERROR: Can't import binary crate!
```

Solution: Split logic into `lib.rs` (testable) and keep `main.rs` as thin wrapper.

