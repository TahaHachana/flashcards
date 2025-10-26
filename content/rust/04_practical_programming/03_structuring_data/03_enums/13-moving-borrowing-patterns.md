## Moving vs Borrowing in Pattern Matching

What's the difference between matching on an enum directly vs matching on a reference to it?

---

**Matching directly** - moves non-Copy data:
```rust
let opt = Some(String::from("hello"));

match opt {
    Some(s) => println!("{}", s),  // s takes ownership
    None => {},
}
// Can't use opt anymore - value moved
```

**Matching on reference** - borrows data:
```rust
let opt = Some(String::from("hello"));

match &opt {
    Some(s) => println!("{}", s),  // s is &String
    None => {},
}
println!("{:?}", opt);  // Still valid - opt not moved
```

**Alternative using ref**:
```rust
match opt {
    Some(ref s) => println!("{}", s),  // ref creates reference
    None => {},
}
println!("{:?}", opt);  // Still valid
```

Use `&opt` or `ref` to avoid moving values out of enums.

