## When to Use Trait Objects

When should you use trait objects instead of generics?

---

Use trait objects when you need:

1. **Heterogeneous collections** - storing different types together
   ```rust
   let shapes: Vec<Box<dyn Shape>> = vec![Box::new(Circle), Box::new(Square)];
   ```

2. **Runtime polymorphism** - type determined at runtime
   ```rust
   let shape = if user_choice { Box::new(Circle) } else { Box::new(Square) };
   ```

3. **Smaller binary size** - one function instead of monomorphized versions

4. **Dynamic plugin systems** - loading types at runtime

Use generics when:
- Performance is critical (no virtual call overhead)
- Types known at compile time
- Need to use generic methods or return `Self`

