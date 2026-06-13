## Execute Command Usage

How do you use `execute` to run a command built from a variable?

---

`execute "colorscheme " . colorScheme` — quoted text stays literal (note the trailing space), and the bare variable `colorScheme` is evaluated and substituted.

