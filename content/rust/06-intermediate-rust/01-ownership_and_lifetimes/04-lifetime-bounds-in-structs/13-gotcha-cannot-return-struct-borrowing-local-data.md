## Gotcha Cannot Return Struct Borrowing Local Data

Why won't this compile, and what are the fixes?
```rust
impl<'a> Container<'a> {
    fn from_string(s: String) -> Container<'a> {
        Container { data: &s }
    }
}
```

---

`s` is owned by the function and dropped at the end, so you can't return a struct that borrows from it. Fixes: (1) Take a reference as input: `fn from_ref(s: &'a str) -> Container<'a>`, or (2) Change struct to own data: `struct Container { data: String }`. Structs can only borrow from data that outlives them.

