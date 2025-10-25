## Pop Method Return Type

What does `.pop()` return and why is this design safer than panicking?

---

`.pop()` returns `Option<T>`: `Some(value)` if the vector has elements, `None` if empty. This forces you to handle the empty case explicitly instead of panicking, making your code safer.

