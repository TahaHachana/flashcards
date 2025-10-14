## if Without else Return Value

What does an if expression return when there's no else and the condition is false?

---

It returns the unit type ().

```rust
let value = if false { 5 };  // value is ()
```

