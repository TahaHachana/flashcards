## Common Enum Patterns Summary

What are five common use cases for enums in Rust?

---

1. **Optional values**: `Option<T>` for nullable data
   - Replaces null with type-safe alternative

2. **Error handling**: `Result<T, E>` for fallible operations
   - Forces explicit error handling

3. **State machines**: Each variant represents a state
   - Compiler ensures all states handled

4. **Message types**: Different message kinds with different data
   - Clean API for varied payloads

5. **Making invalid states unrepresentable**:
   - Use type system to prevent logical errors
   - Different variants have appropriate data

**Key principle**: If data can be "one of several alternatives," use an enum. The compiler will ensure you handle all cases.

