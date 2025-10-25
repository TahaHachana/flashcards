## Single Quotes vs Double Quotes

What is the difference between single quotes and double quotes in command line arguments?

---

Single quotes (`'`) and backticks interpret content literally without expansions (e.g., `'%{cursor_line}'` prints literally).
Double quotes (`"`) support expansions within the quoted content (e.g., `"%{cursor_line}"` expands to the line number).

