## Optimization Differences

What optimization opportunities exist with static dispatch that don't exist with dynamic dispatch?

---

**Static dispatch enables**:
- **Inlining**: Compiler can inline small functions into caller
- **Specialization**: Optimize for specific type's characteristics
- **Dead code elimination**: Remove branches that never execute for a type
- **Constant folding**: Evaluate at compile time

**Dynamic dispatch limitations**:
- **No inlining**: Function call always indirect through vtable
- **Conservative optimization**: Must work for any implementation
- **Runtime indirection**: Always requires vtable lookup

```rust
// Static: Can be fully inlined and optimized
fn process<T: Compute>(value: T) -> i32 {
    value.compute() + 1
}

// Dynamic: Requires vtable lookup, cannot inline
fn process(value: &dyn Compute) -> i32 {
    value.compute() + 1
}
```

