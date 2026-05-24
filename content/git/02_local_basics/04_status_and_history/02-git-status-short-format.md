## git status Short Format

In `git status -s`, what does the output `MM src/app.py` mean? What do the two columns represent?

---

Each line in short format has two columns: **XY filename**

```
X = index (staging area) status
Y = working tree status

M  = modified    A = added    D = deleted
?? = untracked   ' ' = unmodified
```

`MM src/app.py` means:

```
First M  (X column) → index has staged modifications
                       (index differs from HEAD)

Second M (Y column) → working tree has FURTHER modifications
                       (working tree differs from the staged version)
```

In other words, some changes to `app.py` are staged, and additional edits were made after staging. Only the staged portion will appear in the next commit.

