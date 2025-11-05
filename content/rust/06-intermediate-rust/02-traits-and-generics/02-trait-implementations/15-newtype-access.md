## Accessing Wrapped Type in Newtype

In a newtype pattern, how do you access the wrapped value?

---

Access the inner value using `.0` (tuple struct field access):

```rust
struct MyVec(Vec<i32>);

impl Display for MyVec {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "{:?}", self.0)  // Access with .0
    }
}

impl MyVec {
    fn push(&mut self, value: i32) {
        self.0.push(value);  // Access inner Vec with .0
    }
}
```

`.0` refers to the first (and only) field in the tuple struct.

