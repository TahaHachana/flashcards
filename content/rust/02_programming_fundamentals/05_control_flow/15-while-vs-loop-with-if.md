## while vs loop with if

What is the relationship between while loops and loop with if?

---

They're equivalent. while is cleaner syntax for conditional looping.

```rust
while condition { }
// Equivalent to:
loop {
    if !condition { break; }
}
```

