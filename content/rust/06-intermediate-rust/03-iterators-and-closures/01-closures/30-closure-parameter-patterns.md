## Closure Parameter Patterns

Can closures use pattern matching in their parameters? Show examples of destructuring in closure parameters.

---

Yes, closure parameters support full pattern matching, just like function parameters.

**Tuple destructuring:**
```rust
let pairs = vec![(1, 2), (3, 4), (5, 6)];
pairs.iter().for_each(|(a, b)| {
    println!("{} + {} = {}", a, b, a + b);
});
```

**Struct destructuring:**
```rust
struct Point { x: i32, y: i32 }

let points = vec![Point { x: 1, y: 2 }, Point { x: 3, y: 4 }];
points.iter().for_each(|Point { x, y }| {
    println!("({}, {})", x, y);
});
```

**Reference patterns:**
```rust
let numbers = vec![1, 2, 3];

// Dereference in parameter
numbers.iter().for_each(|&n| {
    println!("{}", n); // n is i32, not &i32
});

// Compared to:
numbers.iter().for_each(|n| {
    println!("{}", n); // n is &i32
});
```

**Nested patterns:**
```rust
let data = vec![(1, (2, 3)), (4, (5, 6))];
data.iter().for_each(|(a, (b, c))| {
    println!("{} {} {}", a, b, c);
});
```

Pattern matching in closures makes iterator operations more expressive and concise.

