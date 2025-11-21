## Closure Capture Optimization

How does the compiler optimize what a closure captures? Does it capture entire variables or just what's needed?

---

The compiler is smart about closure captures - it only captures what the closure actually uses.

**Captures only used fields:**
```rust
struct Data {
    x: i32,
    y: String,
    z: Vec<i32>,
}

let data = Data {
    x: 5,
    y: String::from("hello"),
    z: vec![1, 2, 3],
};

// Only captures data.x, not the entire struct
let closure = || println!("{}", data.x);
```

**Captures by smallest necessary scope:**
```rust
let tuple = (1, String::from("hello"), vec![1, 2]);

// Only captures tuple.0, not entire tuple
let get_first = || tuple.0;
```

**However, with `move`:**
```rust
// Moves entire struct, even if only using one field
let closure = move || println!("{}", data.x);
// All of data is moved into closure
```

**Key insight:** Without `move`, compiler does "precision capturing" by automatically borrowing only what's needed. With `move`, entire variables are moved even if partially used.

This optimization reduces closure size and minimizes borrow checker conflicts.

