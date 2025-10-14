## for Loop Over Ranges

How do you use ranges in for loops?

---

Use .. for exclusive ranges or ..= for inclusive ranges.

```rust
for i in 1..5 {
    println!("{}", i);  // 1, 2, 3, 4
}
for i in 1..=5 {
    println!("{}", i);  // 1, 2, 3, 4, 5
}
```

