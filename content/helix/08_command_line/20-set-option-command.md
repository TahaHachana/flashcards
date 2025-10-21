## Set Option Command

How does `:set-option` parse its arguments?

---

The first argument (config option name) is parsed normally. The second argument is interpreted as a string for string options, and everything else is parsed as JSON.

