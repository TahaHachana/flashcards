## Reversed Range

How do you iterate over a range in reverse with a `for` loop?

---

Call `.rev()` on the range.

```rust
for n in (1..=3).rev() {
    println!("{n}");
}
// prints 3, 2, 1
```

