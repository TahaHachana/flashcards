## Why Execute Is Needed

Why does `colorscheme colorScheme` fail when `colorScheme` is a variable?

---

The `colorscheme` command expects a literal scheme name, not a variable, so it tries to load a scheme literally named "colorScheme" and errors. You need `execute` to evaluate the variable first.

