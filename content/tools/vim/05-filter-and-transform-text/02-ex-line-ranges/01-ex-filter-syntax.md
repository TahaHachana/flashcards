## ex Filter Syntax

What is the general syntax for filtering a range of lines through a shell command from the ex (`:`) prompt?

---

`:range!command` — a line address or range, then `!`, then the shell command. The command's output replaces the addressed lines.

