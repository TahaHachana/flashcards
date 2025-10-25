## UTF-8 Self-Synchronizing Property

What does it mean that UTF-8 is self-synchronizing?

---

If you jump to a random position in UTF-8 data, you can quickly find the next character boundary by looking at the byte's high bits. The encoding structure allows you to determine if a byte is:
- A single-byte character (starts with 0)
- The start of a multi-byte character (starts with 11)
- A continuation byte (starts with 10)

This makes error recovery and random access easier.

