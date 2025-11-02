## The Static Lifetime

What does the `'static` lifetime mean, and when is it used?

---

`'static` is a special lifetime meaning "lives for the entire program duration". It's used for:
- String literals: `let s: &'static str = "hello";` (stored in program binary)
- Static constants: `const MAX: i32 = 100;`
- Global variables

It's NOT the same as owned data—`String::from("hello")` is owned but not `'static`.

