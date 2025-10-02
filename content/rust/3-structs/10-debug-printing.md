## Debug Printing

How do you enable debug printing for structs?

---

Add `#[derive(Debug)]` to the struct.
Use `{:?}` for debug and `{:#?}` for pretty debug.

```rust
#[derive(Debug)]
struct Rectangle { width: u32, height: u32 }

println!("rect1 is {:?}", rect1);
```

