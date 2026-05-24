## Line Ending Configuration

How should you configure `core.autocrlf` on Windows vs. macOS/Linux, and why?

---

```
OS            | Setting | Behavior
--------------|---------|-------------------------------------------
Windows       | true    | LF → CRLF on checkout; CRLF → LF on commit
macOS / Linux | input   | CRLF → LF on commit; no change on checkout
```

This prevents line ending conflicts in cross-platform teams where Windows uses CRLF and Unix systems use LF.

```bash
# Windows
git config --global core.autocrlf true

# macOS / Linux
git config --global core.autocrlf input
```

