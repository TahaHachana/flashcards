## Line Ending Configuration

What line ending configuration should you use for Git on Windows vs Mac/Linux, and why does this matter?

---

- Windows: `git config --global core.autocrlf true`
- Mac/Linux: `git config --global core.autocrlf input`

This ensures consistent line endings across different operating systems. Windows uses CRLF (\r\n), while Unix-based systems use LF (\n). The autocrlf setting automatically converts between them.

