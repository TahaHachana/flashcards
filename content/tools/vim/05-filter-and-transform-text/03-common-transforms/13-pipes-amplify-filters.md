## Pipes Amplify Filters

How do pipes increase the power of Vim filters?

---

You can chain multiple Unix commands in one filter, e.g. `:%!awk '...' | sort -n`, so the buffer is transformed by the whole pipeline at once.

