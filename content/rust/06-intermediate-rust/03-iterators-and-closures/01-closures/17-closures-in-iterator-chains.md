## Closures in Iterator Chains

Show how closures are used in iterator chains. What makes them ideal for this use case?

---

Closures are the primary tool for iterator operations:

```rust
let numbers = vec![1, 2, 3, 4, 5];

let result: Vec<i32> = numbers
    .iter()
    .filter(|&&x| x % 2 == 0)    // Keep evens
    .map(|&x| x * x)              // Square them
    .collect();

println!("{:?}", result); // [4, 16]
```

**Why closures are ideal here:**

1. **Inline definition** - Logic written where it's used
2. **Capture context** - Can reference outer variables if needed
3. **Type inference** - Compiler figures out parameter types
4. **Zero overhead** - Closures inline at compile time
5. **Composable** - Chain multiple operations naturally

**Common patterns:**
```rust
.map(|x| x * 2)           // Transform each item
.filter(|x| x > 10)       // Keep items matching condition
.for_each(|x| println!("{}", x))  // Side effect on each
.fold(0, |acc, x| acc + x)        // Reduce to single value
```

Closures make iterator chains concise and expressive.

