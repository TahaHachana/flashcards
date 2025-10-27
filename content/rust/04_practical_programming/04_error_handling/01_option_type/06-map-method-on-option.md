## Map Method On Option

How does the `map()` method work on `Option<T>`?

---

`map()` applies a function to the value inside `Some`, returning a new `Option`. If the original is `None`, it returns `None`:

```rust
let maybe_number = Some(5);
let doubled = maybe_number.map(|n| n * 2);  // Some(10)

let nothing: Option<i32> = None;
let result = nothing.map(|n| n * 2);  // None
```

It transforms the value without unwrapping.

