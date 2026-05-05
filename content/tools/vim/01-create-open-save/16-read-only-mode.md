## Read-Only Mode

How do you open a file in read-only mode and what are the two commands to do it?

---

```
$ vim -R file
$ view file
```

Both open the file in read-only mode. You can navigate and search normally but Vim will refuse any write command. To override and save anyway (if you have permission), use:
```
:w!    or    :wq!
```

If you do not own the file, those overrides will still fail.

