## Basic Closure Syntax

What is the basic syntax for defining a closure in Rust? Show both expression and block forms.

---

Expression form:
```rust
|parameters| expression
```

Block form:
```rust
|parameters| {
    // statements
    expression
}
```

Examples:
```rust
let add_five = |x| x + 5;
let add = |x, y| x + y;
let complex = |x| {
    let doubled = x * 2;
    doubled + 1
};
```

Closures use vertical pipes `||` for parameters, unlike functions which use parentheses `()`.

