## Match Guards

What are match guards and how do you use them?

---

Match guards add extra conditions to patterns using `if`:

```rust
let num = Some(4);

match num {
    Some(x) if x < 5 => println!("less than five: {}", x),
    Some(x) => println!("{}", x),
    None => (),
}

// With multiple patterns
let x = 4;
let y = false;

match x {
    4 | 5 | 6 if y => println!("yes"),  // Matches 4, 5, or 6 AND y is true
    _ => println!("no"),
}
```

**Use cases**:
- Testing additional conditions beyond pattern structure
- Comparing against outer variables
- More complex logic than patterns alone can express

The guard applies after the pattern matches, adding an extra boolean check.

