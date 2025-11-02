## When to Split Lifetimes

What's the guideline for deciding whether to use one lifetime or multiple lifetimes in a function signature?

---

Start with one lifetime for all references, then split only when needed. Split when:
- Return is tied to only one input (not all)
- Inputs have genuinely independent validity requirements
- Using one lifetime creates unnecessarily strict constraints

The single-lifetime approach is simpler and often sufficient.

