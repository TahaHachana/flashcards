## Use Statements Don't Change Visibility

If you write `use some_module::Item;` in a module, can other modules use that import?

---

**No** - `use` only brings items into the current scope, it doesn't change visibility.

**Example**:
```rust
mod my_module {
    use std::collections::HashMap;  // Only in my_module's scope
    
    pub fn create_map() -> HashMap<String, i32> {
        HashMap::new()  // HashMap available here
    }
}

fn main() {
    let map = HashMap::new();  // ERROR: HashMap not in scope
}
```

**To make available to others**: Use `pub use`
```rust
mod my_module {
    pub use std::collections::HashMap;  // Now external code can use it
}

use my_module::HashMap;  // Works!
```

**Key principle**: `use` is about convenience within one scope, not about exposing items to other scopes.

