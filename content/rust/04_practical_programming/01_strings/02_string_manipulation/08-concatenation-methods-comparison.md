## Concatenation Methods Comparison

Compare the three concatenation methods: +, format!, and push_str/push in terms of ownership, performance, and when to use each.

---

+ operator: Moves left, borrows right. Fast. Use for two strings.
format!: Borrows all. Allocates new string. Use for multiple strings or clarity.
push_str/push: Requires mutable. Fast (in-place). Use for building incrementally.

