# Shadowing vs Mutating

What's the difference between shadowing and mutating a variable?

---

- **Shadowing**: Creates a new variable (can change type): `let x = "hello"; let x = x.len();`
- **Mutating**: Changes existing variable's value (same type): `let mut x = 5; x = 6;`