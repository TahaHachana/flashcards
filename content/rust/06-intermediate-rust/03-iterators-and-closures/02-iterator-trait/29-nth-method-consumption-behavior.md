## Nth Method Consumption Behavior

Explain the surprising behavior of `.nth()`. What does it actually do to the iterator?

---

`.nth(n)` doesn't just return the element at index n - it consumes all elements up to and including index n, advancing the iterator.

**Surprising behavior:**
```rust
let mut iter = vec![0, 1, 2, 3, 4, 5].into_iter();

let third = iter.nth(2);  // Gets element at index 2
println!("{:?}", third);   // Some(2)

let next = iter.nth(0);    // Gets NEXT element (3), not element 0!
println!("{:?}", next);    // Some(3)

let skip_one = iter.nth(1); // Skips 4, returns 5
println!("{:?}", skip_one); // Some(5)
```

**What's happening:**
```rust
Initial: [0, 1, 2, 3, 4, 5]
         ^
         
iter.nth(2): Consumes 0, 1, 2 → returns Some(2)
Remaining: [3, 4, 5]
           ^

iter.nth(0): Gets element at current position 0 → returns Some(3)
Remaining: [4, 5]
           ^

iter.nth(1): Skips 4, gets element at position 1 → returns Some(5)
Remaining: []
```

**Key insights:**
- `.nth(n)` means "give me element at position n **from here**"
- It's NOT absolute indexing from the start
- Consumes n+1 elements total
- Can't go backwards

**Better mental model:**
```rust
iter.nth(0) ≈ iter.next()
iter.nth(1) ≈ { iter.next(); iter.next() }
iter.nth(n) ≈ { skip n items; return next }
```

**Use `.skip()` for clarity:**
```rust
// Instead of multiple .nth() calls:
iter.skip(5).next()  // Clearer than iter.nth(5)
```

