## Closure vs Function Distinction

What are the key differences between closures and regular functions in Rust?

---

**Closures:**
- Can capture environment variables
- Have anonymous, unique types
- Type inference for parameters and return values
- Each closure has its own distinct type
- Implement `Fn`, `FnMut`, or `FnOnce` traits
- Syntax: `|params| expression`

**Functions:**
- Cannot capture environment
- Have explicit, named types
- Require explicit type annotations
- Same signature = same type
- Function pointers (`fn` type)
- Syntax: `fn name(params) -> Type { }`

**Example showing difference:**
```rust
fn add_function(x: i32, y: i32) -> i32 { x + y }

let z = 10;
let add_closure = |x, y| x + y + z; // Can capture z

// add_function cannot access z
// add_closure has different type than add_function
```

Closures sacrifice type clarity for flexibility and convenience.

