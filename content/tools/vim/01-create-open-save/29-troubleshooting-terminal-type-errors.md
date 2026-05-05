## Troubleshooting — Terminal Type Errors on Opening

What do messages like "Unknown terminal type" or "Not a typewriter" mean when starting Vim, and what is a quick workaround?

---

These messages mean the `$TERM` environment variable is undefined, set to an unknown value, or the terminal's terminfo entry is broken.

Quick workaround:
- Type `:q` to exit, then set: `export TERM=vt100` (or `setenv TERM vt100` in csh).
- Re-invoke Vim. vt100 is a basic but widely supported terminal type.

For a lasting fix, investigate the terminfo database or consult the system documentation.

