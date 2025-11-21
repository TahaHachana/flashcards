## Closure Capture and Ownership Rules

What ownership rules apply to captured variables? Can you use a moved value after a closure captures it?

---

Closures must follow Rust's ownership rules:

**With borrowing (default):**
```rust
let x = String::from("hello");
let print = || println!("{}", x);
print();
println!("{}", x); // OK - x was borrowed
```

**With move:**
```rust
let x = String::from("hello");
let consume = move || println!("{}", x);
consume();
// println!("{}", x); // ERROR - x was moved
```

**Key rules:**

1. **Immutable borrows** - Multiple closures can borrow immutably
2. **Mutable borrows** - Only one closure can borrow mutably
3. **Move captures** - Variable can't be used after being moved
4. **Copy types** - Can use after `move` (copied, not moved)

```rust
let n = 5; // i32 is Copy
let closure = move || println!("{}", n);
closure();
println!("{}", n); // OK - n was copied
```

The closure inherits the captured variable's ownership semantics.

