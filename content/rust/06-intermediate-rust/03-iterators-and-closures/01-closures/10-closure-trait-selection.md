## Closure Trait Selection

How does the Rust compiler decide which Fn trait to implement for a closure?

---

The compiler automatically selects based on what the closure does with captured variables:

**Decision flow (tries most flexible first):**

1. **Fn** - If closure only reads captured variables
   ```rust
   let x = 5;
   let read = || println!("{}", x); // Implements Fn
   ```

2. **FnMut** - If closure mutates captured variables
   ```rust
   let mut x = 5;
   let mutate = || x += 1; // Implements FnMut (not Fn)
   ```

3. **FnOnce** - If closure moves/consumes captured variables
   ```rust
   let x = String::from("hi");
   let consume = || drop(x); // Implements FnOnce only
   ```

You cannot manually choose - it's determined by the closure's behavior. The compiler picks the most permissive trait that's safe.

