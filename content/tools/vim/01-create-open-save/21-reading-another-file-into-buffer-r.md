## Reading Another File into the Buffer — :r

How do you insert the contents of another file into the file you are currently editing?

---

```
:r filename         → insert file after the current cursor line
:185r filename      → insert file after line 185
:$r filename        → insert file at the very end
:0r filename        → insert file at the very beginning (before line 1)
:/pattern/r file    → insert file after the line matching pattern
```

The `:r` command (short for `:read`) inserts the entire named file starting on the line after the given address.

