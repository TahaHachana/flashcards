# Ownership in Function Calls

How does ownership transfer when passing arguments to functions?

---

- Passing a non-`Copy` type moves ownership.  
- Passing a `Copy` type duplicates the value.

```rust
fn takes_ownership(s: String) { /* s dropped here */ }
fn makes_copy(x: i32)      { /* x is Copy */ }

let s = String::from("rust");
takes_ownership(s); // s moved → invalid after

let x = 42;
makes_copy(x);      // x copied → still valid
println!("{}", x);  // prints 42
```