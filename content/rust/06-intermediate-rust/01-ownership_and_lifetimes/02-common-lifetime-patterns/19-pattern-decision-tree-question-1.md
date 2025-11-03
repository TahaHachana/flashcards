## Pattern Decision Tree Question 1

Using the pattern decision tree, what pattern applies to a function that takes two references and returns a bool?

---

Pattern 5 (No Output References). Since the function doesn't return a reference, the input lifetimes are independent and usually don't need to be related. Example: `fn compare<'a, 'b>(x: &'a str, y: &'b str) -> bool`. In practice, these lifetimes are often elided.

