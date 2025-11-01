## Best Practices Summary

What are the key best practices for using paths and `use` statements in Rust?

---

**Best practices**:

1. **Import style**:
   - Functions: via parent (`use std::fmt;` → `fmt::Display`)
   - Types: directly (`use std::collections::HashMap;`)

2. **Avoid glob imports** (`*`) except in:
   - Test modules (`use super::*;`)
   - Prelude modules

3. **Use aliases** for name conflicts:
   ```rust
   use std::io::Result as IoResult;
   ```

4. **Group related imports**:
   ```rust
   use std::{fs::File, io::Read};
   ```

5. **Flatten APIs with `pub use`**:
   ```rust
   pub use internal::deeply::nested::Item;
   ```

6. **Choose paths wisely**:
   - Absolute (`crate::`) for clarity
   - Relative (`super::`) for nearby modules

7. **Remember the order**: `mod` declares, then `use` imports

8. **Keep traits in scope** to use their methods

**Golden rule**: Prioritize clarity and consistency over brevity.

