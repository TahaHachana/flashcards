## Pattern 1 Parsing and Text Processing

What are the characteristics of the parsing/text processing pattern with struct lifetimes?

---

The struct holds a reference to input data (like `input: &'a str`) along with position/state. Methods return slices of that input, and all returned references have the same lifetime `'a` as the input. This enables zero-copy parsing—working with slices of the original input without allocation. Example: `Parser<'a>` with methods returning `&'a str`.

