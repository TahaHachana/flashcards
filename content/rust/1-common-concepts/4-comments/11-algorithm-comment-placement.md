# Algorithm Comment Placement

Where should you place a comment explaining a complex algorithm?

---

Above the code block, before the algorithm starts:
```rust
// Implement quicksort algorithm
// Time complexity: O(n log n) average case
fn quicksort(arr: &mut [i32]) {
    // implementation
}
```