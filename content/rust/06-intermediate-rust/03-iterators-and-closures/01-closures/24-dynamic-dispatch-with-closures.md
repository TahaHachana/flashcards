## Dynamic Dispatch with Closures

What is the difference between `Box<dyn Fn()>` and `impl Fn()` for closures? When would you use each?

---

**`impl Fn()` (static dispatch):**
```rust
fn take_closure(f: impl Fn()) {
    f();
}
```
- Compile-time type resolution
- Monomorphization (separate code per closure type)
- Zero runtime overhead
- Cannot store in collections or structs easily
- Most common and preferred

**`Box<dyn Fn()>` (dynamic dispatch):**
```rust
fn take_closure(f: Box<dyn Fn()>) {
    f();
}
```
- Runtime type resolution (vtable lookup)
- Single compiled version of function
- Small runtime cost (pointer indirection)
- Can store different closure types together
- Heap allocation

**Use `impl Fn()` when:**
- Performance matters
- Don't need to store closures
- Known at compile time

**Use `Box<dyn Fn()>` when:**
- Storing different closures in a collection
- Need to return closures with different types
- Building callback systems

```rust
let callbacks: Vec<Box<dyn Fn()>> = vec![
    Box::new(|| println!("A")),
    Box::new(|| println!("B")),
];
```

