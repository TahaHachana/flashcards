## Peekable Iterator

What does `.peekable()` do? How does `.peek()` differ from `.next()`?

---

`.peekable()` converts an iterator into a `Peekable` iterator that lets you look at the next element without consuming it.

**Creating peekable:**
```rust
let mut iter = vec![1, 2, 3].into_iter().peekable();
```

**`.peek()` vs `.next()`:**

**`.peek()` - Look without consuming:**
```rust
let mut iter = vec![1, 2, 3].into_iter().peekable();

// Peek multiple times
println!("{:?}", iter.peek()); // Some(&1)
println!("{:?}", iter.peek()); // Some(&1) - still there!
println!("{:?}", iter.peek()); // Some(&1)

// Now consume it
println!("{:?}", iter.next()); // Some(1)
println!("{:?}", iter.peek()); // Some(&2) - next element
```

**Conditional processing:**
```rust
let mut iter = numbers.into_iter().peekable();

while let Some(&value) = iter.peek() {
    if value > 10 {
        break;  // Stop without consuming
    }
    println!("{}", iter.next().unwrap());
}
```

**Grouping elements:**
```rust
while let Some(&current) = iter.peek() {
    let mut group = vec![iter.next().unwrap()];
    
    while let Some(&next) = iter.peek() {
        if next == current {
            group.push(iter.next().unwrap());
        } else {
            break;
        }
    }
    println!("Group: {:?}", group);
}
```

**Key insight:** `.peek()` returns `Option<&Item>` (reference), allowing inspection without ownership transfer.

