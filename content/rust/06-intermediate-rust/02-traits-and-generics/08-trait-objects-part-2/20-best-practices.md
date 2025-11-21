## Best Practice Summary

What are the three key best practices for choosing between static and dynamic dispatch?

---

1. **Start with trait objects (dynamic dispatch)**
   - Simpler code
   - Smaller binaries
   - Easier to understand
   - Optimize only if profiling shows bottleneck

2. **Use generics for library APIs**
   - Give users maximum performance
   - Let them choose their own trade-offs
   - Zero-cost abstraction

3. **Profile before optimizing**
   - Measure actual performance
   - Don't assume dynamic dispatch is "too slow"
   - Optimize hot paths only

```rust
// ✅ Start here (simple)
fn process(item: &dyn Handler) { }

// ✅ Switch if profiling shows bottleneck
fn process<T: Handler>(item: &T) { }
```

**Remember**: Premature optimization is the root of all evil. The 2-5ns overhead rarely matters.

