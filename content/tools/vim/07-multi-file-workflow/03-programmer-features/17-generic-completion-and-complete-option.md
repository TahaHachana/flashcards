## Generic Completion And Complete Option

What does `CTRL-N` (generic completion) do, and where are its sources defined?

---

It combines all the other searches into one, with sources defined in the `complete` option (e.g. `.` current buffer, `w` other windows, `b` loaded buffers, `k` dictionary, `s` thesaurus, `i` included files, `t`/`]` tags).

