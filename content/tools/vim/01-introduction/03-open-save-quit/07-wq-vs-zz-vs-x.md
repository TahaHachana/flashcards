## wq Versus ZZ Versus x

How do :wq, ZZ, and :x differ in when they write?

---

:wq writes unconditionally (always updating the modification time). ZZ and :x write only if the file was actually changed. The timestamp difference matters to tools like make.

