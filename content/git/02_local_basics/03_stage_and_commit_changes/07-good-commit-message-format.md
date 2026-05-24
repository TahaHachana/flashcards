## Good Commit Message Format

What are the three structural rules for a well-formed Git commit message, and why does each matter?

---

```
Rule 1 — Subject line: imperative mood, ≤ 50 characters
  "Add login validation"  not  "Added login validation"
  Why: shown in git log --oneline, GitHub PR titles, email
       subjects — brevity makes it scannable.

Rule 2 — Blank line between subject and body
  Why: tools (git log, GitHub, email clients) use it to
       distinguish subject from body. Without it, the body
       is treated as part of the subject.

Rule 3 — Body lines wrapped at 72 characters, explaining WHY
  Why: the diff already shows what changed; the message
       should record the intent, rationale, or constraints
       that made the change necessary.
```

