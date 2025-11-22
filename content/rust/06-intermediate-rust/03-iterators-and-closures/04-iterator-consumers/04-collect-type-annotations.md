## Collect Type Annotations

Why does `.collect()` require type annotations? Show all four ways to provide them.

---

`.collect()` is generic over the output type, so the compiler needs hints about what to build.

**Why:** Can produce Vec, HashSet, HashMap, String, Result, Option, etc.

**Four ways to provide type:**

**1. Variable type annotation:**
```rust
let result: Vec<i32> = iter.collect();
```

**2. Turbofish syntax:**
```rust
let result = iter.collect::<Vec<i32>>();
```

**3. Partial inference (underscore):**
```rust
let result = iter.collect::<Vec<_>>();
// Compiler infers inner type
```

**4. Context from usage:**
```rust
fn process(v: Vec<i32>) { }

process(iter.collect());  // Type inferred from parameter
```

**Without annotation - error:**
```rust
let result = iter.collect();  
// ERROR: type annotations needed
```

**Best practice:** Use variable annotation for clarity at declaration, turbofish when chaining.

The flexibility is a feature - one method for all collection types - but requires explicit type information.

