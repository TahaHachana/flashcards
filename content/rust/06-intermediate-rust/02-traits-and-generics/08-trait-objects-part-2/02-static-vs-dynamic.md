## Static vs Dynamic Dispatch

What is the fundamental difference between static and dynamic dispatch?

---

**Static dispatch (generics)**:
- Compiler generates specialized code for each type
- Direct function calls, can be inlined
- Zero runtime overhead
- Larger binary size

**Dynamic dispatch (trait objects)**:
- One function handles all types
- Indirect calls through vtable
- Small runtime overhead (~2-5 nanoseconds)
- Smaller binary size

```rust
// Static: Compiler generates separate code for each type
fn process<T: Display>(value: T) { }

// Dynamic: One function, type determined at runtime
fn process(value: &dyn Display) { }
```

