## Lazy Iterator Evaluation

What does "iterators are lazy" mean? Give an example.

---

Iterators don't execute until consumed. They build a plan but do nothing:
```rust
vec.iter().map(|x| x * 2);  // ⚠️ Does nothing!

// Must consume:
let result: Vec<i32> = vec.iter()
    .map(|x| x * 2)
    .collect();  // Now it executes
```
Compiler warns: "iterators are lazy and do nothing unless consumed"

