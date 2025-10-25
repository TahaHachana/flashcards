## Recursive Shell Expansion

How are variables within shell expansions evaluated?

---

Shell expansions are evaluated recursively—variables within the shell expansion are evaluated first, before executing the shell command. For example, `%sh{echo '%{buffer_name}:%{cursor_line}'}` executes `echo 'README.md:1'`.

