## git status Short Format

What does `git status -s` output and what do the status codes mean?

---

`git status -s` shows condensed status with codes:
- `??` = Untracked
- `A` = Added (new file, staged)
- `M` = Modified
- `D` = Deleted
- `R` = Renamed
- First column = staging area status
- Second column = working directory status

Example: `MM file.txt` = Modified, staged, then modified again

