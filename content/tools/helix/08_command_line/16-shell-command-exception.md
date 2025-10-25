## Shell Command Exception

What is special about how commands like `:insert-output`, `:pipe`, and `:run-shell-command` handle arguments?

---

These commands support expansions but pass arguments directly to the shell without interpreting quotes. For example, `:sh echo "%{buffer_name}"` passes `echo "README.md"` to the shell—expansions are evaluated but quotes are not.

