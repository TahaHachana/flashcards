## Gotcha Methods Cannot Return References to Locals

Why won't this method compile, and what are the two ways to fix it?

```rust
impl Container {
    fn get_uppercase(&self) -> &str {
        let upper = self.data.to_uppercase();
        &upper  // upper dropped here!
    }
}
```

---

`upper` is a local variable that gets dropped at the end of the method, so you can't return a reference to it. Two fixes: (1) Return owned data: `fn get_uppercase(&self) -> String { self.data.to_uppercase() }`, or (2) Return reference to existing data in self: `fn get_data(&self) -> &str { &self.data }`. Methods can only return references to data that outlives the method call.

