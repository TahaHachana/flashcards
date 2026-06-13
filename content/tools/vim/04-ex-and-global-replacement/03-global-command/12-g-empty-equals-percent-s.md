## g Empty Substitute Equals Percent s

What plain substitute command is equivalent to `:g/editer/s//editor/g`?

---

`:%s/editer/editor/g`. They have the same effect; the `:%s` form is shorter when the find-pattern and the change-pattern are identical.

