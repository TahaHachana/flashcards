## When to Use &str

List five scenarios when you should use &str instead of String.

---

1. When you're reading string data (read-only access)
2. For function parameters (when you don't need ownership)
3. When you don't need ownership of the data
4. When you want maximum flexibility (works with String, literals, slices)
5. When you want to avoid unnecessary allocations

