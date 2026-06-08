## Character Versus Line Deletion

How does deleting with `d/pattern` differ from the ex command `:.,/pattern/d`?

---

`d/pattern` deletes character-by-character, only the text between the cursor and the match. `:.,/pattern/d` deletes the entire range of lines.

