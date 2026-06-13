## Read Output At The Top Of File

How do you place the output of `:r !cmd` at the very top of the file?

---

Precede it with line address `0`: `:0r !cmd`. A line address before `:r` controls where the output is inserted.

