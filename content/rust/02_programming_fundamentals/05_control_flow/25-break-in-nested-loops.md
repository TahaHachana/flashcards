## break in Nested Loops

How do you break out of multiple nested loops at once?

---

Use labeled break with the outer loop's label.

```rust
'outer: for i in 1..=3 {
    for j in 1..=3 {
        if i == 2 && j == 2 {
            break 'outer;
        }
    }
}
```

