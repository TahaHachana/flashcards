## The :w Command — Save Without Quitting

What ex command saves the buffer to disk without quitting Vim, and when should you use it?

---

`:w` (write) saves the buffer to disk but keeps the editing session open.

You should use `:w` regularly throughout an editing session to protect your work against system failure or a major accidental edit. It does not quit the editor.

