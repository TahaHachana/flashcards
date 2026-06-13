## Pipes Inside A Filter Command

Can you use shell pipes inside a Vim filter command?

---

Yes. Pipes work normally, so you can chain Unix tools, e.g. `:%!awk '...' | sort -n` replaces the whole buffer with the chained output.

