## Deriving Debug Trait

Why can't you print a struct by default and how do you fix it?

---

Structs don't implement the Debug trait by default, so `println!("{:?}", struct)` fails.

**Solution**: Derive the Debug trait:

```rust
#[derive(Debug)]
struct Point {
    x: f64,
    y: f64,
}

let p = Point { x: 1.0, y: 2.0 };
println!("{:?}", p);       // Point { x: 1.0, y: 2.0 }
println!("{:#?}", p);      // Pretty-printed version
```

The `#[derive(Debug)]` attribute tells the compiler to automatically generate a Debug implementation.

