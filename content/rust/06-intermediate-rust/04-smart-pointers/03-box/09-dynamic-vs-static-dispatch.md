## Dynamic vs Static Dispatch

Explain the difference between static and dynamic dispatch, and when each is used. What does the `dyn` keyword indicate?

---

**Static dispatch (compile-time):**
```rust
fn static_dispatch<T: Animal>(animal: T) {
    animal.speak();  // Compiler knows exact type
}
```
- Compiler generates specific code for each type
- Faster (no indirection)
- Used with generics
- Code size grows with each concrete type

**Dynamic dispatch (runtime):**
```rust
fn dynamic_dispatch(animal: Box<dyn Animal>) {
    animal.speak();  // Type determined at runtime
}
```
- Compiler generates code to look up methods in vtable at runtime
- Slight performance overhead (one extra indirection)
- Used with trait objects
- Enables returning different types from function

**The `dyn` keyword:**
- Explicitly indicates **dyn**amic dispatch
- Shows you're working with a trait object, not a concrete type
- Required syntax: `dyn Trait` not just `Trait`

**When to use dynamic dispatch:** Returning different types, heterogeneous collections, plugin systems.

