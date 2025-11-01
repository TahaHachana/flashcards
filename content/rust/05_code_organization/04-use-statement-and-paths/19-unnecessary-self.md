## Unnecessary Self Paths

When is `self::` necessary in paths, and when is it redundant?

---

**Usually unnecessary** - `self::` is implicit for relative paths:
```rust
use my_module::MyType;       // Implicit self::
use self::my_module::MyType; // Explicit (redundant)
```

**When `self::` is needed**: Disambiguating conflicts
```rust
mod internal {
    pub struct Config {}
}

use external_crate::Config;  // From external crate
use self::internal::Config;  // From our crate (disambiguates)
```

**Better pattern**: Use aliases instead
```rust
use external_crate::Config as ExternalConfig;
use internal::Config;

let external = ExternalConfig::new();
let internal = Config::new();
```

**Best practice**: Omit `self::` unless needed for clarity.

