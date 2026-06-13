## Why The Dot Loop Is Safe

Why might the `n` / `.` loop be preferable to a global `:%s` substitution?

---

It lets you confirm each occurrence before changing it and skip the ones that shouldn't change — useful when only some matches should be edited.

