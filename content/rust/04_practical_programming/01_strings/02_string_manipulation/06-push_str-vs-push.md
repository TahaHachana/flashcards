## Push_str vs Push

What's the difference between push_str and push methods?

---

push_str appends a string slice:
```rust
let mut s = String::from("foo");
s.push_str("bar");  // "foobar"
```

push appends a single character:
```rust
let mut s = String::from("lo");
s.push('l');  // "lol"
```

Both modify the String in place without new allocation (unless capacity is exceeded).

