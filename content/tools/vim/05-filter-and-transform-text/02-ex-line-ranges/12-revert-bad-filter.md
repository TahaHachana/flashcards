## Reverting A Bad Filter

After saving with `:w`, what ex command reloads the last-saved version if a filter mangles the buffer?

---

`:e!` — it discards unsaved changes and reloads the file from disk.

