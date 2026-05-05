## Appending Part of a File to Another File

What syntax appends lines from the current buffer to an existing file instead of overwriting it?

---

Use `>>` with the write command:

```
:1,10w newfile         → write lines 1–10 to newfile (creates or overwrites)
:340,$w >> newfile     → append from line 340 to end to newfile
```

After these two commands, newfile contains lines 1–10 followed by lines 340 to the end of the buffer.

