## Breaking Out of Loops

How do you exit a loop early?

---

Use the break keyword.

```rust
let mut count = 0;
loop {
    count += 1;
    if count == 5 {
        break;
    }
}
```

