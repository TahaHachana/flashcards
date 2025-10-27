## And Then Method

What is `and_then()` used for with `Option<T>` and how does it differ from `map()`?

---

`and_then()` chains operations that themselves return `Option`. It's used when the transformation function returns an `Option`:

```rust
Some(10)
    .and_then(|n| divide(n, 2))  // divide returns Option
    .and_then(|n| divide(n, 5))  // can chain multiple operations
```

Unlike `map()` (which wraps the result in `Some`), `and_then()` expects the function to return an `Option`, preventing nested `Option<Option<T>>`.

