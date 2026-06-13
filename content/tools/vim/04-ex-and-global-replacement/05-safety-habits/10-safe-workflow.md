## A Safe Substitution Workflow

Describe a safe workflow for a large global change.

---

```
:w                    checkpoint the file
:%s/\<old\>/new/gc    scoped, whole-word change with confirmation
:e!                   if it goes wrong, revert to the checkpoint
```

