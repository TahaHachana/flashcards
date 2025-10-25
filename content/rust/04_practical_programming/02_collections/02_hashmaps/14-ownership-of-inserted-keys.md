## Ownership of Inserted Keys

What happens to ownership when you insert a String key and String value into a HashMap?

---

Ownership is **moved** into the HashMap (for non-Copy types). After insertion, you can no longer use the original variables:
```rust
let key = String::from("k");
let val = String::from("v");
map.insert(key, val);
// key and val are now moved, cannot use them
```

