## Closure Equivalence and Comparison

Can you compare or check equality between closures? Why or why not?

---

No, you cannot compare closures for equality in Rust. Closures don't implement `PartialEq` or `Eq`.

**This doesn't work:**
```rust
let a = |x| x + 1;
let b = |x| x + 1;

// ERROR: binary operation `==` cannot be applied
// if a == b { }
```

**Why closures can't be compared:**

1. **Each closure is a unique type** - Even identical-looking closures are different types
2. **Captured state is opaque** - No standard way to compare captured variables
3. **Semantic equality is ambiguous** - Should `|x| x + 1` equal `|y| y + 1`?

**Workaround - compare results:**
```rust
let a = |x| x + 1;
let b = |x| x + 1;

// Compare what they produce
if a(5) == b(5) {
    println!("Same result for this input");
}
```

**Or use function pointers for comparability:**
```rust
fn add_one(x: i32) -> i32 { x + 1 }
fn add_two(x: i32) -> i32 { x + 2 }

let f: fn(i32) -> i32 = add_one;
let g: fn(i32) -> i32 = add_one;

if f == g { // OK - function pointers are comparable
    println!("Same function");
}
```

