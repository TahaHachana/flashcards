## When Generics Are Zero-Cost

Explain monomorphization and why it makes generics zero-cost.

---

**Monomorphization**: The compiler generates specialized versions of generic code for each concrete type used.

```rust
fn process<T>(value: T) {
    // generic code
}

fn main() {
    process(5);        // i32 version generated
    process("hello");  // &str version generated
}

// Compiler effectively creates:
// fn process_i32(value: i32) { }
// fn process_str(value: &str) { }
```

**Why zero-cost**: At runtime, the code is already specialized. No lookups, no indirection, no overhead. It's as if you wrote separate functions manually.

Trade-off: Larger binary size (more code generated), but no runtime cost.

