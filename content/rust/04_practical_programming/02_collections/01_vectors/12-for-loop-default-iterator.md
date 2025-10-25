## For Loop Default Iterator

When you write `for item in vec`, which iterator method is implicitly called?

---

`.into_iter()` - the for loop takes ownership and consumes the vector. To keep the vector, explicitly use `for item in &vec` (calls `.iter()`) or `for item in &mut vec` (calls `.iter_mut()`).

