## Elision Order of Application

In what order does the compiler apply the three elision rules?

---

The compiler applies the rules in order: Rule 1, then Rule 2, then Rule 3. If all lifetimes can be determined after applying these rules, elision succeeds. If any ambiguity remains, you must write explicit annotations. The rules are mechanical and deterministic—there's no guessing or AI involved.

