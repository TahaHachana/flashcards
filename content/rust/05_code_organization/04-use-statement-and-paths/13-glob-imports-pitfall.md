## Glob Imports Pitfall

What's the problem with glob imports (`*`), and when should you use them?

---

**Problem**: Makes it unclear where items come from
```rust
use std::collections::*;
use my_module::*;

let map = HashMap::new();  // From std? From my_module? Unclear!
```

**When glob is acceptable**:
1. **Test modules**: `use super::*;`
2. **Prelude modules**: `use std::prelude::v1::*;`
3. **Internal code** where you control the namespace

**When to avoid**:
- Public API or library code
- When modules might have overlapping names
- When clarity matters more than brevity

**Better alternative**:
```rust
use std::collections::HashMap as StdHashMap;
use my_module::HashMap as MyHashMap;

let map1 = StdHashMap::new();  // Clear!
let map2 = MyHashMap::new();   // Clear!
```

