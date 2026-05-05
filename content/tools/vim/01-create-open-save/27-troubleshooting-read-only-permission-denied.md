## Troubleshooting — Read Only or Permission Denied

Vim shows "[Read only]" or "Permission denied" when you try to write. What are the possible causes and fixes?

---

Causes:
- Vim was launched with `view` or `vim -R` (read-only mode).
- You do not have write permission for the file.

Fixes:
- If you own the file and have permission, use `:w!` or `:wq!` to force the write.
- If you lack write permission, use `:w /tmp/myfile` to save a copy to a directory where you do have permission, then adjust permissions externally.
- If the file system is full, first free space or use `:pre` to preserve the swap file.

