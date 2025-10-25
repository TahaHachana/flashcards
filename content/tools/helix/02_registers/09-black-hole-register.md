## Black Hole Register

What is the purpose of the `_` register in Helix?

---

The `_` register is a "black hole" register. When read, it returns no values. When written to, all values are discarded. Use it for deletions you don't want to store (e.g., `"_d`).

