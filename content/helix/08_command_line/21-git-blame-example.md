## Git Blame Example

What does this keybinding do: `":echo %sh{git blame -L %{cursor_line},+1 %{buffer_name}}"`?

---

It prints the git blame information for the current line to the statusline. The variables expand to line number and filename, then the shell executes git blame for that specific line.

