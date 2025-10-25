## Creating Empty HashMap

Write code to create an empty HashMap that maps String keys to i32 values.

---

```rust
use std::collections::HashMap;

let mut map: HashMap<String, i32> = HashMap::new();
```
Or let Rust infer from first insertion:
```rust
let mut map = HashMap::new();
map.insert(String::from("key"), 10);
```

