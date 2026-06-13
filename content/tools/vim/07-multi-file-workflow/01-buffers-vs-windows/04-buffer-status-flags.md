## Buffer Status Flags

What do the buffer status flags shown by `:ls` mean?

---

```
Flag   Meaning
-----  --------------------------------------------------
u      Unlisted buffer (shown only with !)
%      Buffer in the current window
#      Alternate buffer (switch with :e #)
a      Active (loaded and visible)
h      Hidden (loaded but not visible)
-      modifiable off (read-only)
=      Read-only and cannot be made modifiable
+      Modified (unsaved changes)
x      Read errors
```

