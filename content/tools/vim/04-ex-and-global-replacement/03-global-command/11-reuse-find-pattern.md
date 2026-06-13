## Reusing The Find Pattern

When the line-finding pattern is the same string you want to change, how can you avoid typing it twice?

---

Leave the substitute pattern empty. `:g/string/s//new/g` finds lines containing `string` and replaces that same `string` with `new`.

