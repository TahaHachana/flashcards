## NLL Practical Impact

How do Non-Lexical Lifetimes improve usability?

---

References end when you're done using them, not at scope boundaries. Allows operations after a reference's last use.

```rust
let first = &vec[0];
println!("{}", first);  // Last use
vec.push(4);  // ✅ OK with NLL
```

