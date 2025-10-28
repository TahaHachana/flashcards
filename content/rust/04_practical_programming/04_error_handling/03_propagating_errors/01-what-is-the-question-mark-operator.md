## What Is The Question Mark Operator?

What is the `?` operator in Rust and what problem does it solve?

---

The `?` operator is syntactic sugar for propagating errors up the call stack. It's the idiomatic way to handle errors in Rust.

It solves the problem of verbose error propagation by replacing repetitive match statements with clean, readable syntax. Instead of manually checking and returning errors, `?` automatically unwraps success values or returns errors.

It's a zero-cost abstraction that compiles to the same code as manual propagation.

