## Public API Sufficiency Test

How do integration tests enforce good API design?

---

Integration tests force you to verify your public API is sufficient:

If tests can't accomplish something:
```rust
// tests/test.rs
#[test]
fn test_workflow() {
    let data = my_project::Data::new();
    // ❌ Can't inspect internal state
    // ❌ Can't test intermediate steps
    let result = my_project::process(data);
}
```

This reveals API gaps:
```rust
// src/lib.rs
pub struct Data {
    value: i32,  // Private, no getter
}

impl Data {
    pub fn new() -> Self { Data { value: 0 } }
    // Missing: pub fn value(&self) -> i32
    // Missing: pub fn set_value(&mut self, v: i32)
}
```

Solution: Add necessary public methods:
```rust
impl Data {
    pub fn value(&self) -> i32 { self.value }
    pub fn set_value(&mut self, v: i32) { self.value = v; }
}
```

Integration tests ensure your API is complete and usable.

