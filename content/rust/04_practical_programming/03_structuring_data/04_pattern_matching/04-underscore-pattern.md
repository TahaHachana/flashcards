## The Underscore Pattern

What is the difference between _ and a named variable starting with _ in patterns?

---

**`_` (underscore)**: Doesn't bind, no ownership taken
```rust
let opt = Some(String::from("hello"));

if let Some(_) = opt {
    println!("Got something");
}
println!("{:?}", opt);  // OK - opt not moved
```

**`_name` (underscore prefix)**: Does bind, takes ownership
```rust
let opt = Some(String::from("hello"));

if let Some(_s) = opt {
    println!("Got something");
}
// println!("{:?}", opt);  // ERROR - value moved to _s
```

**Use `_`** when you don't need the value. The underscore prefix is for variables you want to bind but the compiler warns are unused.

You can also ignore parts: `let (x, _, z) = (1, 2, 3);`

