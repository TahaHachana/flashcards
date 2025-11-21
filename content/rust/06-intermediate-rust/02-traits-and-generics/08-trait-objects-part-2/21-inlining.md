## Inlining and Dynamic Dispatch

Why can't the compiler inline methods called through trait objects?

---

The compiler **doesn't know which concrete function will be called** until runtime:

```rust
fn process(shape: &dyn Shape) {
    shape.area();  // Which area()? Circle's? Square's?
}
```

**Static dispatch** (can inline):
```rust
fn process<T: Shape>(shape: &T) {
    shape.area();  // Compiler knows exact type T
    // Can inline Circle::area() or Square::area()
}
```

**Why inlining matters**:
- Eliminates function call overhead
- Enables further optimizations (constant folding, dead code elimination)
- Can turn small functions into just a few instructions

**Impact**: For tiny methods called frequently, inlining makes a big difference. For larger methods, less important.

