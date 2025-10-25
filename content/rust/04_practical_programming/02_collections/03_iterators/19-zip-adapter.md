## Zip Adapter

What does `.zip()` do? Show an example creating a HashMap.

---

Combines two iterators into tuples:
```rust
use std::collections::HashMap;

let keys = vec!["a", "b", "c"];
let values = vec![1, 2, 3];

let map: HashMap<_, _> = keys.into_iter()
    .zip(values.into_iter())
    .collect();
// {"a": 1, "b": 2, "c": 3}
```

