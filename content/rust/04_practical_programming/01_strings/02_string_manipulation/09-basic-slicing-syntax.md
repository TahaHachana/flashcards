## Basic Slicing Syntax

What does this slicing code produce?
```rust
let s = String::from("hello world");
let hello = &s[0..5];
let world = &s[6..11];
```

---

hello = "hello" (characters from index 0 to 4)
world = "world" (characters from index 6 to 10)

Range syntax [start..end] is exclusive of end. Slicing extracts parts without copying the data - it creates borrowed views.

