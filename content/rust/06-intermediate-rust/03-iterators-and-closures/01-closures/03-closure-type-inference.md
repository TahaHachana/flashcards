## Closure Type Inference

How does type inference work for closures, and what happens after the first use?

---

Closures infer parameter and return types from usage, unlike functions which require explicit types.

```rust
let multiply = |x, y| x * y;
let result = multiply(5, 6); // Infers i32
```

**Important**: Once types are inferred from first use, they're locked in permanently:

```rust
let identity = |x| x;
let s = identity(String::from("hi")); // Locks to String -> String
// let n = identity(5); // ERROR: expects String, not i32
```

You can provide explicit types if needed:
```rust
let divide = |x: f64, y: f64| -> f64 { x / y };
```

