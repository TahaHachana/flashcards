## g Flag Versus g Command

What is the difference between the `g` flag in `:s///g` and the `:g` command?

---

The `g` flag affects each matching pattern on a single line. The separate `:g` command selects each line of the file that matches a pattern. They are different mechanisms that share the letter g.

