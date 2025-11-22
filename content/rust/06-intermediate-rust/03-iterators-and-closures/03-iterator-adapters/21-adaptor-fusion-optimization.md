## Adaptor Fusion Optimization

Explain how multiple iterator adaptors fuse into a single pass. Why doesn't chaining create multiple loops?

---

Multiple adaptors fuse through compiler optimizations, creating a single loop that checks all conditions per element.

**Example chain:**
```rust
let result: Vec<i32> = data.iter()
    .filter(|&&x| x > 0)
    .map(|&x| x * 2)
    .filter(|&x| x < 100)
    .map(|x| x + 1)
    .collect();
```

**What beginners might expect (wrong):**
```rust
// Intermediate collections (NOT what happens)
let temp1 = data.iter().filter(...).collect::<Vec<_>>();
let temp2 = temp1.iter().map(...).collect::<Vec<_>>();
let temp3 = temp2.iter().filter(...).collect::<Vec<_>>();
let result = temp3.iter().map(...).collect::<Vec<_>>();
```

**What actually compiles to (right):**
```rust
let mut result = Vec::new();
for &x in data.iter() {
    if x > 0 {                    // First filter
        let x = x * 2;            // First map
        if x < 100 {              // Second filter
            let x = x + 1;        // Second map
            result.push(x);
        }
    }
}
```

**How fusion works:**

1. **Type nesting:** Each adaptor wraps previous:
   ```rust
   Map<Filter<Map<Filter<Iter<i32>>>>>
   ```

2. **Inlining:** All closures inline completely

3. **Single .next() chain:** Each `.next()` calls next on inner:
   ```rust
   Map::next() 
     → calls Filter::next()
       → calls Map::next()
         → calls Filter::next()
           → calls Iter::next()
   ```

4. **LLVM optimization:** Flattens nested calls into single loop

**Performance result:**
- Zero intermediate allocations
- Single pass through data
- Same assembly as hand-written loop
- No function call overhead

**This is why "zero-cost abstraction" is real** - the high-level functional code costs nothing at runtime.

