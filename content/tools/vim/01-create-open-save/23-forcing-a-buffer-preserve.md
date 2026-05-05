## Forcing a Buffer Preserve — :preserve

What ex command forces Vim to save the swap file immediately, and when is it useful?

---

`:pre` (short for `:preserve`)

This forces Vim to write the current buffer to its swap file right away, even without a crash. It is useful when:
- The filesystem is full and you cannot write the file normally.
- You lack write permission for the file and want to ensure your edits are not lost.

After `:pre`, you can look for space to free or use `:w pathname/file` to write elsewhere.

