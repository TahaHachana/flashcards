## Saving Part of a File with Line Addressing

How do you write only a range of lines from the current buffer to a new file?

---

Combine ex line addresses with `:w`:

```
:230,$w newfile      → save from line 230 to end of file
:.,600w newfile      → save from current line to line 600
:1,50w header.txt    → save lines 1–50
```

The `.` symbol means the current line, and `$` means the last line of the file.

