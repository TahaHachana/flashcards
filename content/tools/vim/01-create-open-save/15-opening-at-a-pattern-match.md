## Opening a File at a Pattern Match

How do you open a file so that the cursor lands on the first line matching a given pattern?

---

```
$ vim -c /pattern file
```

Example: `vim -c /TODO notes.txt` opens notes.txt with the cursor positioned at the first line containing "TODO."

If the pattern contains spaces, quote it or escape the spaces:
```
vim -c /"fix this" file
vim -c /fix\ this file
```

