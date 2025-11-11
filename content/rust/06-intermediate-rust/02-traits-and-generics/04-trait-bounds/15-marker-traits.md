## Marker Trait Bounds

What are marker traits and how are they used in trait bounds?

---

Marker traits have no methods but provide compile-time guarantees. Common examples: `Send`, `Sync`, `Copy`.

```rust
fn process<T: Send + Sync>(value: T) {
    // T can be safely sent between threads (Send)
    // T can be safely shared between threads (Sync)
}
```

**Send**: Type can be transferred between threads
**Sync**: Type can be shared between threads via references
**Copy**: Type can be implicitly copied

Even with no methods, these traits tell the compiler about safety properties.

