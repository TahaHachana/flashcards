## Opening a File at a Specific Line Number

What command-line options open a file at a specific line number or at the last line?

---

```
$ vim -c n file    → opens file at line number n
$ vim + file       → opens file at the very last line
```

The `-c` flag (or the older `+` prefix) executes a command immediately after the file is loaded. Example: `vim -c 42 report.txt` opens report.txt with the cursor on line 42.

