## Module Organization Best Practices

What are the key best practices for organizing code with modules and visibility?

---

**Best practices**:

1. **Start private, make public as needed**
   - Don't pre-emptively make everything public
   - Add `pub` when you get compiler errors

2. **Group related functionality**
   ```rust
   pub mod database {
       pub mod users { /* ... */ }
       pub mod posts { /* ... */ }
   }
   ```

3. **Keep implementation details private**
   - Only expose what users need
   - Hide internal helpers and state

4. **Use constructors for validation**
   ```rust
   pub struct Email(String);  // Private field
   
   impl Email {
       pub fn new(s: String) -> Result<Self, Error> {
           // Validate before constructing
       }
   }
   ```

5. **Use `#[cfg(test)]` for test modules**
   - Keeps tests close to code
   - Tests can access private items

6. **Be cautious with glob imports**
   - Use mainly in tests: `use super::*;`
   - Prefer explicit imports in production code

