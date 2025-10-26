## Patterns in let Statements

How are let statements actually pattern matching, and what kinds of destructuring can you do?

---

Every `let` statement uses pattern matching:

```rust
// Simple binding (pattern: x)
let x = 5;

// Destructure tuples
let (x, y, z) = (1, 2, 3);

// Destructure structs
struct Point { x: i32, y: i32 }
let Point { x, y } = Point { x: 0, y: 7 };

// Ignore values
let (first, _, third) = (1, 2, 3);

// Rest pattern
let (first, .., last) = (1, 2, 3, 4, 5);
// first=1, last=5, middle ignored
```

**Note**: `let` requires **irrefutable patterns** (patterns that always match). Can't use `let Some(x) = opt` because it might be None.

