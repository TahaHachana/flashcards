## Closure Definition and Purpose

What is a closure in Rust and what are its three main purposes?

---

A closure is an anonymous function that can capture variables from its surrounding environment.

Three main purposes:
1. **Inline behavior** - Define functions directly where needed without naming them
2. **Environment capture** - Access variables from surrounding scope without passing as parameters
3. **Functional programming** - Enable operations like map, filter, fold

Closures bridge the gap between functions (stateless) and data by allowing functions to "remember" their context.

