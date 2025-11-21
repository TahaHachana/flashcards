## Closure and Copy Types

How do `Copy` types behave differently in closures compared to non-`Copy` types? Show the difference with `move`.

---

`Copy` types are implicitly copied when captured, even with `move`, while non-`Copy` types are moved.

**Copy types (primitives, etc.):**
```rust
let x = 5; // i32 is Copy
let closure = move || println!("{}", x);
closure();
println!("{}", x); // OK - x was copied, not moved
```

**Non-Copy types:**
```rust
let s = String::from("hello"); // String not Copy
let closure = move || println!("{}", s);
closure();
// println!("{}", s); // ERROR - s was moved
```

**Mixed scenario:**
```rust
let num = 42;        // Copy
let text = String::from("hi"); // Not Copy

let closure = move || {
    println!("{} {}", num, text);
};

closure();
println!("{}", num);   // OK - num was copied
// println!("{}", text); // ERROR - text was moved
```

**Key insight:** The `move` keyword doesn't change semantics for `Copy` types. They're still copied, just into the closure's storage. For non-`Copy` types, `move` transfers ownership.

This is why you can use integers after `move` but not `String` or `Vec`.

