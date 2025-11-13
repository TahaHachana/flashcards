## Three Key Benefits of Generics

What are the three key benefits of using generic types?

---

1. **Code reuse**: Write once, use with many types
   ```rust
   fn id<T>(x: T) -> T { x }  // Works with any type
   ```

2. **Type safety**: Compiler ensures type correctness at compile time
   ```rust
   let x: Vec<i32> = vec![1, 2, 3];
   // Can't accidentally add a String
   ```

3. **Zero runtime cost**: Generic code is specialized at compile time (monomorphization)
   ```rust
   // No runtime overhead compared to hand-written versions
   ```

You get flexibility without sacrificing performance or safety.

