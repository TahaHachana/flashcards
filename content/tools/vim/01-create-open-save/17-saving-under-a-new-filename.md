## Saving Under a New Filename

How do you save the current buffer as a different filename, leaving the original file unchanged?

---

```
:w newfilename
```

This writes the buffer to newfilename. The original file is untouched (provided you did not previously write to it). You can then quit with `:q` without affecting the original.

Example — to save practice as practice.new:
```
:w practice.new
```

