## Overriding Write Warnings — :w!

In what two situations is `:w!` needed, and what does the exclamation point do?

---

The `!` overrides Vim's protective warnings. It is needed when:

1. Writing to an existing file that would be overwritten (Vim warns "File exists").
2. Writing a file opened in read-only mode (vim -R or view), provided you have filesystem write permission.

Examples: `:w!` (overwrite current file), `:wq!` (write and quit), `:w! newfile` (force write to newfile).

