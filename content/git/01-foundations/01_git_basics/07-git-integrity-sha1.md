## Git Integrity via SHA-1

How does Git ensure the integrity of stored data?

---

Everything in Git is checksummed with a **SHA-1 hash** — a 40-character hexadecimal string — before being stored. Git refers to everything by this hash. It is impossible to change any file or directory content without Git detecting it. Example hash:

`24b9da6552252987aa493b52f8696cd6d3b00373`

