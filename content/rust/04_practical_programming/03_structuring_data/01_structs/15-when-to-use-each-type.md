## When to Use Each Struct Type

Given these scenarios, which struct type should you use: (1) modeling a user with name and email, (2) wrapping a single value for type safety, (3) implementing a trait without data?

---

1. **Classic struct** - User with name and email
   ```rust
   struct User { name: String, email: String }
   ```
   Use when fields have clear, distinct meanings.

2. **Tuple struct** - Wrapping for type safety
   ```rust
   struct UserId(u64);
   ```
   Use for "newtype" pattern or when field names are obvious.

3. **Unit struct** - Trait implementation without data
   ```rust
   struct Logger;
   impl LogTrait for Logger { /* ... */ }
   ```
   Use when you need a type but no data storage.

