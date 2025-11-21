## Closure Capture and Partial Moves

Can a closure capture some fields of a struct by move and others by reference? What happens with partial moves?

---

No, closures cannot do partial moves - they capture entire variables, not individual fields.

**This doesn't work:**
```rust
struct Data {
    x: String,
    y: i32,
}

let data = Data {
    x: String::from("hello"),
    y: 42,
};

// Want to move x, borrow y? Can't do directly:
// let closure = move || {
//     println!("{}", data.x); // moves x
//     println!("{}", data.y); // wants to move y too
// };
```

**Workaround - destructure first:**
```rust
let Data { x, y } = data;

let closure = move || {
    println!("{}", x); // moves x
    // y is separate, can still use it
};

println!("{}", y); // OK
```

**Or shadow with references:**
```rust
let x_ref = &data.x;
let closure = move || println!("{}", x_ref); // moves reference
// data.y still accessible
```

The `move` keyword applies to all captured variables atomically. For fine-grained control, destructure or create separate bindings before the closure.

