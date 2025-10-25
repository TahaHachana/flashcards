## System Clipboard Register

What is the `+` register used for in Helix?

---

The `+` register interacts with the system clipboard. When read, it reads from the system clipboard. When written to, it joins selections with newlines and yanks to the system clipboard (like Ctrl+C/Ctrl+V).

