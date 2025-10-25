## Collect Into HashMap

How do you collect an iterator of tuples into a HashMap?

---

```rust
use std::collections::HashMap;

let pairs = vec![("a", 1), ("b", 2), ("c", 3)];

let map: HashMap<_, _> = pairs
    .into_iter()
    .collect();

// Or from separate iterators:
let map: HashMap<_, _> = keys.into_iter()
    .zip(values)
    .collect();
```

