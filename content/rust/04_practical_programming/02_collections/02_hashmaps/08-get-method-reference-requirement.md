## Get Method Reference Requirement

Why do you write `map.get(&1)` instead of `map.get(1)` when the key is an integer?

---

The `.get()` method signature is `fn get(&self, key: &K)` - it takes a reference to the key, not an owned key. This avoids unnecessary moves/clones. Use `&1` or `&key_variable` when calling `.get()`.

