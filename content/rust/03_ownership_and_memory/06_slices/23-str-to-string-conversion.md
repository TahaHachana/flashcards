## &str to String Conversion

How do you convert &str to String?

---

Multiple ways: to_string(), String::from(), or to_owned().

```rust
let slice = "hello";
let owned = slice.to_string();
let owned = String::from(slice);
let owned = slice.to_owned();
```

