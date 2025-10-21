## Manual Drop Function

How do you manually drop a value before end of scope?

---

Use std::mem::drop function. It takes ownership and drops immediately.

```rust
let s = String::from("hello");
drop(s);  // s dropped immediately
// s is invalid after this
```

