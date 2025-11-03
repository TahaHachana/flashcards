## Pattern Decision Tree Question 3

Using the pattern decision tree, what pattern applies to a function that takes two string references and returns one of them based on a condition?

---

Pattern 2 (Multiple Sources, Same Lifetime). Since the return could be either input, both must have the same lifetime and the return shares that lifetime. Example: `fn choose<'a>(x: &'a str, y: &'a str, cond: bool) -> &'a str`. This ensures both inputs live long enough for the return value.

