## Troubleshooting — [New File] When You Expected an Existing File

Vim shows "[New file]" but you expected to open an existing file. What should you check?

---

1. Case sensitivity — Unix filenames are case-sensitive. `Letter.txt` and `letter.txt` are different files.
2. Wrong directory — use `:q` to quit, then run `pwd` in the shell to verify your current directory.
3. Wrong name — run `ls` in the shell to see all files in the directory and confirm the exact name.

Correct the error and re-invoke Vim with the right path or filename.

