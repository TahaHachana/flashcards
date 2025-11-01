## External Crate Paths

How do paths work for external crates, and how do you import from them?

---

**External crate paths** start with the crate name:

**In Cargo.toml**:
```toml
[dependencies]
serde = "1.0"
tokio = "1.0"
```

**In code**:
```rust
use serde::{Serialize, Deserialize};
use tokio::runtime::Runtime;
//    ^^^^^  ^^^^^^^ ^^^^^^^^
//    crate  module  item
```

**Structure**:
- First part: Crate name (from Cargo.toml)
- Rest: Path within that crate's module tree

**Multiple items**:
```rust
use serde::{Serialize, Deserialize, Serializer};
use tokio::{
    runtime::Runtime,
    sync::Mutex,
    time::sleep,
};
```

**Key point**: External crates are accessed just like the `std` crate—by their name followed by their internal path.

