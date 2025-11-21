## When to Use Dynamic Dispatch

When should you use dynamic dispatch (trait objects) instead of static dispatch?

---

Use **dynamic dispatch (trait objects)** when:

1. **Need heterogeneous collections**
   ```rust
   let shapes: Vec<Box<dyn Shape>> = vec![
       Box::new(Circle),
       Box::new(Square),
   ];
   ```

2. **Type determined at runtime**
   ```rust
   fn create_shape(shape_type: &str) -> Box<dyn Shape> {
       match shape_type {
           "circle" => Box::new(Circle),
           "square" => Box::new(Square),
           _ => panic!(),
       }
   }
   ```

3. **Binary size matters** (embedded systems, WASM)

4. **Plugin/extensibility systems**

5. **Performance difference is negligible** (most code)

