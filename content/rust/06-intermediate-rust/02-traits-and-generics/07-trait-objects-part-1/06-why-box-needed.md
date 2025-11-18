## Why Box Is Required

Why can't you return `dyn Trait` directly? Why is `Box<dyn Trait>` needed?

---

Traits don't have a known size at compile time because different types implementing the trait can have different sizes:

```rust
struct Small { x: u8 }        // 1 byte
struct Large { data: [u8; 1000] }  // 1000 bytes

impl MyTrait for Small { }
impl MyTrait for Large { }

// ❌ Size unknown - doesn't compile
fn returns_trait() -> dyn MyTrait { /* ... */ }

// ✅ Box has known size (8 bytes on 64-bit)
fn returns_trait() -> Box<dyn MyTrait> {
    Box::new(Small { x: 5 })
}
```

`Box` provides a fixed-size pointer while the actual data lives on the heap.

