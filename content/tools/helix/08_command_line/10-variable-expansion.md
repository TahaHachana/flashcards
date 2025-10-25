## Variable Expansion

How do you expand a variable in the command line?

---

Use `%{variable_name}` without specifying a kind. For example, `%{cursor_line}` expands to the current line number, so `:echo %{cursor_line}` might print `1`.

