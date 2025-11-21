## Zero-Cost Abstractions

How do generics exemplify Rust's "zero-cost abstraction" principle?

---

Static dispatch through generics has **literally zero runtime cost** compared to hand-written specialized code:

```rust
fn print<T: Display>(value: T) {
    println!("{}", value);
}

// After monomorphization, this is as fast as:
fn print_i32(value: i32) {
    println!("{}", value);
}
```

**Why zero-cost**:
- Abstraction (generics) compiles away completely
- Direct function calls (can be inlined)
- Full compiler optimizations apply
- No runtime penalty for using abstraction

**Principle**: You don't pay for abstractions you don't use, and abstractions are as efficient as hand-written code.

