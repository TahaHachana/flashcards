## When to Use Static Dispatch

When should you use static dispatch (generics) instead of dynamic dispatch?

---

Use **static dispatch (generics)** when:

1. **Performance is critical**
   ```rust
   fn hot_path<T: Compute>(data: T) {
       // Called millions of times per second
   }
   ```

2. **Types known at compile time**
   ```rust
   fn process_config(config: Config) { }
   ```

3. **Need generic methods or return Self**
   ```rust
   trait Cloneable {
       fn clone_self(&self) -> Self;  // Not object-safe
   }
   ```

4. **Working with iterators** (they use static dispatch for performance)

**Bottom line**: Use when you need maximum performance and types are known.

