## Shell Expansion

How do you execute a shell command and use its output in the command line?

---

Use `%sh{command}`. The contents are passed to the configured shell. For example, `:echo %sh{echo "20 * 5" | bc}` may print `100` on the statusline.

