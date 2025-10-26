## Three Types of Structs Summary

What are the three types of structs in Rust and provide a one-line example of each?

---

1. **Classic structs** - Named fields
   ```rust
   struct User { username: String, age: u32 }
   ```

2. **Tuple structs** - Unnamed fields accessed by index
   ```rust
   struct Color(u8, u8, u8);
   ```

3. **Unit structs** - No fields at all
   ```rust
   struct Marker;
   ```

Each serves different purposes: classic for most cases, tuple for type distinction, unit for markers and trait implementations.

