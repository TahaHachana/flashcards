## Building HashMap from Vectors

How do you create a HashMap from two vectors (keys and values) using iterators?

---

```rust
let keys = vec!["a", "b", "c"];
let values = vec![1, 2, 3];

let map: HashMap<_, _> = keys.into_iter()
    .zip(values.into_iter())
    .collect();
```
`.zip()` pairs up elements, `.collect()` gathers into HashMap.

