## Position Method

What does `.position()` return and how is it different from `.find()`?

---

`.position()` returns `Option<usize>` with the index of first match:
```rust
let pos = vec![10, 20, 30].iter()
    .position(|&x| x == 20);
// Some(1)
```

`.find()` returns `Option<&T>` with the actual value:
```rust
let val = vec.iter().find(|&&x| x == 20);
// Some(&20)
```

