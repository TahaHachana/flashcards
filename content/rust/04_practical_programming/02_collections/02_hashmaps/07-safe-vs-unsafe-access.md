## Safe vs Unsafe Access

Compare `map["key"]` vs `map.get("key")` for accessing HashMap values.

---

`map["key"]`: Direct indexing, panics if key doesn't exist, returns value directly.

`map.get("key")`: Safe access, returns `Option<&V>` (`Some(&value)` or `None`), never panics.

Best practice: Use `.get()` unless you're certain the key exists.

