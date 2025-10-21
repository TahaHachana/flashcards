## Backslash on Windows

How does the backslash character behave differently on Windows vs Unix?

---

On Unix, backslash can escape spaces, tabs, quotes, and percent at argument beginning. On Windows, backslash is always treated literally. Additionally, `:echo \n` always prints `\n` literally on both systems.

