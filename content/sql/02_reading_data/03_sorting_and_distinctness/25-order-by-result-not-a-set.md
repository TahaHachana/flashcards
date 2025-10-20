## ORDER BY Result Not A Set

Why is an ordered result technically no longer a "set"? Does this matter practically?

---

Sets are unordered by definition (set theory). Once you ORDER BY, result has sequence, so it's not technically a "set" anymore.

Theoretical impact:
- Some operations requiring sets might not work on ordered results
- It's a reminder that ordering is presentation, not data structure

Practical impact:
- Mostly theoretical
- Ordered results work in almost all SQL operations
- You can still use ordered results normally
- It's more of a conceptual distinction

Key insight: ORDER BY transforms data from "set of rows" (unordered) to "sequence of rows" (ordered).

In practice, don't worry about this distinction - just know that ORDER BY changes the fundamental nature of the result from mathematical perspective.

