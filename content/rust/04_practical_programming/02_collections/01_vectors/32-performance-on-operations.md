## Performance O(n) Operations

Which vector operations are O(n) (linear time) and why?

---

- `.remove(index)` - shifts all elements after index left
- `.insert(index, value)` - shifts all elements after index right
- Reallocation - copies all n elements to new memory
- `.contains()` - must check each element

