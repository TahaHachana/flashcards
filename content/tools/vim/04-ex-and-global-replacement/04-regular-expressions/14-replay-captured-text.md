## Replaying Captured Text

Write a substitution that turns "That or this" into "this or That".

---

`:%s/\(That\) or \(this\)/\2 or \1/` — `\1` holds "That", `\2` holds "this", and they are replayed in reversed order.

