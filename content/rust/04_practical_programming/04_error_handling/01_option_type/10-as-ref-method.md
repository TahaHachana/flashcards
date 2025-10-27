## As Ref Method

Why would you use `as_ref()` on an `Option<T>` and what does it do?

---

`as_ref()` converts `Option<T>` to `Option<&T>`, allowing you to work with a reference to the inner value without moving/consuming it:

```rust
let owned = Some(String::from("hello"));
let length = owned.as_ref().map(|s| s.len());
// owned is still usable here!
println!("{:?}", owned);  // Some("hello")
```

Without `as_ref()`, methods like `map()` would consume the owned value.

