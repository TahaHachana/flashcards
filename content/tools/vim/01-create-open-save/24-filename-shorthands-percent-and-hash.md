## Filename Shorthands — % and #

What do the `%` and `#` symbols represent in ex commands that take a filename?

---

```
%  → the current filename (the file currently in the buffer)
#  → the alternate (previous) filename
```

Examples:
```
:w %        → write the buffer to the current file (same as plain :w)
:e #        → switch to editing the previous file
:r #        → read the previous file into the current buffer
```

These shorthands save typing when working with two files back and forth.

