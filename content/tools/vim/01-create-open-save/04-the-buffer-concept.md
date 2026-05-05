## The Buffer Concept

What is a Vim "buffer" and why does it matter for saving?

---

A buffer is a temporary, in-memory copy of the file being edited. All edits are made to the buffer only. The original file on disk is unchanged until you explicitly write (save) the buffer. Writing the buffer copies it back to disk, replacing the old file.

