## Constraint on Struct Instantiation

How do lifetime parameters constrain when struct instances can be created and exist?

---

A struct `Foo<'a>` can only exist during lifetime `'a`—when the referenced data is valid. You can only create instances when the data you're borrowing from is available, and instances must go out of scope before the borrowed data does. The lifetime parameter acts as a constraint that the borrow checker enforces, preventing dangling references by ensuring the struct doesn't outlive its data.

