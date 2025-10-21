## Primary Clipboard Register

What is the `*` register used for in Helix?

---

The `*` register interacts with the primary clipboard (middle-click paste on X11 systems). When read, it reads from the primary clipboard. When written to, it joins selections with newlines and yanks to the primary clipboard.

