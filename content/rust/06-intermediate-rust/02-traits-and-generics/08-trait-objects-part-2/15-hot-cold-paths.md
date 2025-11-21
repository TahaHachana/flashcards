## Hot vs Cold Paths

How should you approach dispatch choice differently for hot paths vs cold paths?

---

**Hot paths** (performance-critical, called frequently):
```rust
// Use static dispatch
fn render_pixel<R: Renderer>(renderer: &mut R, x: u32, y: u32) {
    renderer.draw_pixel(x, y);  // Called millions of times
}
```

**Cold paths** (called infrequently):
```rust
// Use dynamic dispatch
fn handle_ui_event(event: &dyn Event) {
    event.process();  // Called maybe 60 times per second
}
```

**Guidelines**:
- Hot path: Inside loops, graphics rendering, data processing
- Cold path: UI events, error handling, initialization
- When unsure: It's probably a cold path!

Most code is cold paths where dynamic dispatch is fine.

