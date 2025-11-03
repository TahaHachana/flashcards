## Interpreting Elision Compiler Errors

What does this compiler error mean in terms of elision rules?
```
error: missing lifetime specifier
fn example(x: &str, y: &str) -> &str
```

---

This error means: "I applied Rule 1 (gave each input separate lifetimes), but can't determine the output lifetime because Rules 2 and 3 don't apply." Rule 2 doesn't apply (multiple inputs), and Rule 3 doesn't apply (not a method). You need to explicitly specify which input(s) the output lifetime relates to.

