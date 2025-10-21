## Escape Percent Character

How do you escape a percent character in the command line instead of treating it as an expansion?

---

Use two percent characters consecutively: `%%`. For example, to use shell command `date -u +'%Y-%m-%d'`, write `:echo %sh{date -u +'%%Y-%%m-%%d'}`.

