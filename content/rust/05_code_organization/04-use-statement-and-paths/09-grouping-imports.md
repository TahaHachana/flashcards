## Grouping Related Imports

How do you group related imports together in Rust?

---

**Use nested braces `{}`**:
```rust
use std::{
    collections::{HashMap, HashSet},
    fs::File,
    io::{Read, Write},
};
```

**Equivalent to**:
```rust
use std::collections::HashMap;
use std::collections::HashSet;
use std::fs::File;
use std::io::Read;
use std::io::Write;
```

**Benefits**:
- More concise
- Groups related items visually
- Easier to see what's being imported from each module

**Pattern for external crates**:
```rust
use serde::{Serialize, Deserialize};
use tokio::{runtime::Runtime, sync::Mutex};
```

