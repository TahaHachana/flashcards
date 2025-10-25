## HashMap Type Definition

What is the full type signature of a Rust HashMap, and what do K and V represent?

---

`HashMap<K, V>` where K is the key type and V is the value type. Both must be consistent - all keys must be the same type, and all values must be the same type. Example: `HashMap<String, i32>` maps Strings to integers.

