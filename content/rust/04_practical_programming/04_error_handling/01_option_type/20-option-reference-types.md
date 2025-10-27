## Option Reference Types

What's the difference between `Option<&T>` and `&Option<T>`?

---

`Option<&T>`: An Option containing a reference
- You own the Option but not the data
- Can move the Option without cloning the data
- Common return type from methods

`&Option<T>`: A reference to an Option
- Borrowed access to the Option
- Cannot move the inner value out
- Common parameter type

```rust
fn takes_ref_opt(opt: &Option<String>) {
    // Can't move String out
}

fn takes_opt_ref(opt: Option<&String>) {
    // Can pass None or Some with borrowed String
}
```

