## When Performance Actually Matters

Under what specific conditions does the performance difference between static and dynamic dispatch actually matter?

---

Dynamic dispatch overhead matters when **ALL** of these are true:

1. **Called extremely frequently** (millions of times in tight loop)
2. **Method is tiny** (< 10 instructions, would normally be inlined)
3. **Profiler shows it's a bottleneck** (not just assumed)

**Example where it matters**:
```rust
// Inner loop in game engine, called 60M times/second
fn render_frame<R: Renderer>(renderer: &mut R) {
    for pixel in pixels {
        renderer.draw(pixel);  // Tiny method, called millions of times
    }
}
```

**Example where it doesn't matter**:
```rust
// UI event handler, called ~60 times/second
fn handle_click(handler: &dyn ClickHandler) {
    handler.on_click();  // 2ns overhead × 60/sec = irrelevant
}
```

**Rule**: If you haven't profiled it, it probably doesn't matter.

