## Efficient Ownership Transfer with Box

How does `Box` make transferring ownership of large data more efficient?

---

Moving a `Box` only moves the pointer (8 bytes), not the data itself.

**Without Box (inefficient):**
```rust
struct LargeStruct {
    data: [u8; 10_000],
}

fn take_large(s: LargeStruct) {
    // Use s
}

let large = LargeStruct { data: [0; 10_000] };
take_large(large);  // ❌ Copies entire 10,000 bytes
```

**With Box (efficient):**
```rust
fn take_boxed(s: Box<LargeStruct>) {
    // Use s
}

let boxed = Box::new(LargeStruct { data: [0; 10_000] });
take_boxed(boxed);  // ✅ Only copies 8-byte pointer
```

**Benefit:**
- Moving stack value: Copies all bytes
- Moving Box: Copies only pointer (8 bytes)
- Data stays on heap, only ownership of pointer transfers

**Use when:** Frequently moving large structs between functions.

