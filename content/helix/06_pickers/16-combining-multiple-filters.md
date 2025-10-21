## Combining Multiple Filters

What types of filters can be combined in a picker query?

---

You can combine:
- Content filters (fuzzy text or regex)
- Column filters (`%column`)
- Negation (`!`)
- Prefix/suffix matching (`^`, `$`)
Example: `impl %p src/ !test` finds "impl" in src/ directory but not in test files.

