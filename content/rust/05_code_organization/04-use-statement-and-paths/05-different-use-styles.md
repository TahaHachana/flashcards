## Different Styles of Use Statements

What are the different ways to write `use` statements in Rust?

---

**1. Import item directly**:
```rust
use std::collections::HashMap;
let map = HashMap::new();
```

**2. Import parent module**:
```rust
use std::collections;
let map = collections::HashMap::new();
```

**3. Import multiple items**:
```rust
use std::collections::{HashMap, HashSet, BTreeMap};
```

**4. Import with alias**:
```rust
use std::collections::HashMap as Map;
let my_map = Map::new();
```

**5. Import everything (glob)**:
```rust
use std::collections::*;
let map = HashMap::new();
```

**Choose based on**: Clarity, convention, and avoiding conflicts.

