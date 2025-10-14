## for vs while for Iteration

Why is for preferred over while for iteration?

---

for loops are safer and more concise. They eliminate bugs like forgetting to increment index or accessing out of bounds.

```rust
// Using while (error-prone)
let mut i = 0;
while i < arr.len() {
    println!("{}", arr[i]);
    i += 1;
}

// Using for (safer)
for element in arr {
    println!("{}", element);
}
```

