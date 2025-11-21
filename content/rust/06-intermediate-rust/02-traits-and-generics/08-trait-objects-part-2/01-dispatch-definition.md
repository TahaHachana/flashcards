## What Is Dispatch?

What is dispatch in the context of method calls, and what are the two types?

---

**Dispatch** is the process of determining which method implementation to call.

**Two types**:
1. **Static dispatch** - Decision made at compile time
2. **Dynamic dispatch** - Decision made at runtime

```rust
// Static dispatch (generics)
fn process<T: Display>(value: T) {
    println!("{}", value);  // Decision at compile time
}

// Dynamic dispatch (trait objects)
fn process(value: &dyn Display) {
    println!("{}", value);  // Decision at runtime
}
```

The choice between them involves trade-offs between performance, binary size, and flexibility.

