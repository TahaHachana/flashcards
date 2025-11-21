## For Each Method

What does `.for_each()` do? When should you use it instead of a for loop?

---

`.for_each()` consumes an iterator and applies a closure to each element for side effects.

**Basic usage:**
```rust
vec![1, 2, 3].iter().for_each(|x| {
    println!("Value: {}", x);
});
```

**Compared to for loop:**
```rust
// for loop
for x in vec.iter() {
    println!("{}", x);
}

// .for_each()
vec.iter().for_each(|x| println!("{}", x));
```

**When to use `.for_each()` over for loop:**

1. **In iterator chains:**
```rust
vec.iter()
    .filter(|&&x| x > 0)
    .map(|x| x * 2)
    .for_each(|x| println!("{}", x));
```

2. **With method chaining style:**
```rust
data.iter()
    .enumerate()
    .for_each(|(i, x)| println!("{}: {}", i, x));
```

**When to use for loop:**
- Need early break/continue
- More complex control flow
- Better readability for simple cases

**Key difference:**
- `.for_each()` is a consuming method in a chain
- `for` loops are standalone control structures

Both have identical performance - use whichever is more readable for your case.

