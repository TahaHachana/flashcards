## Zero-Cost Abstractions

What does "zero-cost abstraction" mean for generics, and how does Rust achieve it?

---

Zero-cost means using generics has no runtime performance penalty. Rust achieves this through **monomorphization**: the compiler generates specialized code for each concrete type used.

```rust
fn process<T>(value: T) { }

fn main() {
    process(5);        // Compiler generates process_i32
    process("hello");  // Compiler generates process_str
}
```

At compile time, generic code is expanded into multiple specialized versions. At runtime, there's no indirection or overhead - it's as if you wrote separate functions manually.

