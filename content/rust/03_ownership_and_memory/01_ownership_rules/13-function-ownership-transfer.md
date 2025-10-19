## Function Ownership Transfer

What happens to ownership when you pass a String to a function?

---

Ownership moves to the function parameter. The original variable becomes invalid. When the function ends, the value is dropped.

```rust
fn take(s: String) { }
let my_string = String::from("hello");
take(my_string);  // my_string now invalid
```

