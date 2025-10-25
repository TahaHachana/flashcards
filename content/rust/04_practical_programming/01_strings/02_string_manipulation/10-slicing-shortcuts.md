## Slicing Shortcuts

What do these four slicing patterns mean?
```rust
&s[..n]
&s[n..]
&s[..]
&s[start..end]
```

---

[..n] - From start to index n (exclusive)
[n..] - From index n to end
[..] - Entire string
[start..end] - From start to end (exclusive)

Examples:
```rust
let s = String::from("hello");
&s[..2]    // "he"
&s[3..]    // "lo"
&s[..]     // "hello"
&s[1..4]   // "ell"
```

