## Parentheses For Clarity

Why should you always use parentheses when combining AND and OR operators?

---

Parentheses make intent clear and control evaluation order.

Ambiguous:
```sql
WHERE status = 'Active' OR status = 'Pending' AND age >= 18
```

Could mean:
1. Active OR (Pending AND 18+)  ← This is what happens (AND first)
2. (Active OR Pending) AND 18+  ← Maybe what you wanted

Clear with parentheses:
```sql
WHERE (status = 'Active' OR status = 'Pending') AND age >= 18
```

Now there's no ambiguity!

Benefits:
- Makes intent explicit
- Prevents bugs from precedence mistakes
- Makes code more readable
- Works same across all databases

Rule: When mixing AND/OR, use parentheses. Period.

