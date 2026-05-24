## Glob Patterns in .gitignore

Match each pattern to what it ignores:

```
A) *.log
B) debug/*.o
C) **/temp
D) *.py[co]
E) file?.log
```

---

```
A) *.log       → All files ending in .log anywhere in the repo.
                 * does not cross directories, but without a
                 leading slash or path, the pattern applies
                 recursively to all directories.

B) debug/*.o   → .o files directly inside debug/ ONLY.
                 Does not match debug/sub/file.o.

C) **/temp     → Any file or directory named temp at ANY
                 depth. ** crosses directory boundaries.

D) *.py[co]    → Files ending in .pyc or .pyo (character class
                 matches one of the listed characters).

E) file?.log   → file1.log, file2.log, filea.log, etc.
                 ? matches exactly one character.
```

