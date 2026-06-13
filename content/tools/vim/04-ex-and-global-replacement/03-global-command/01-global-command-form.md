## The Global Command Form

What is the form of the global command, and what does it do?

---

`:g/pattern/command` — ex scans the entire buffer, remembers every line matching `pattern`, then executes `command` on each of those lines.

