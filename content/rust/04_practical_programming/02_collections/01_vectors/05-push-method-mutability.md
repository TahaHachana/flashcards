## Push Method Mutability

What happens if you try to use `.push()` on an immutable vector? How do you fix it?

---

It causes a compile error because `.push()` requires `&mut self`. Fix by declaring the vector as mutable: `let mut vec = Vec::new();`

