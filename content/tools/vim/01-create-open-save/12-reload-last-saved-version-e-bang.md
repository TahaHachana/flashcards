## Reload the Last Saved Version — :e!

How do you discard all current edits and reload the last saved version of the file without quitting Vim?

---

`:e!`

This reloads the file from disk, replacing the current buffer contents. All edits since the last write are lost. It is useful when you want to start the current editing session over without exiting Vim.

