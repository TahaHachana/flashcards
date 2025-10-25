## String to &str Conversion

How do you convert String to &str?

---

Multiple ways: &s, &s[..], or s.as_str().

```rust
let s = String::from("hello");
let slice: &str = &s;
let slice = &s[..];
let slice = s.as_str();
```

