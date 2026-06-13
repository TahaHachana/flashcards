## Three Windows Three Buffers Setup

Starting Vim on `file1`, what commands give you three windows showing three different files?

---

`:split file2` followed by `:split file3`. This produces three windows backed by three buffers (file1=1, file2=2, file3=3).

