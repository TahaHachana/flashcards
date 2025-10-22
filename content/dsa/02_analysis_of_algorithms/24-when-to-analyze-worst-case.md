## When to Analyze Worst Case

In what scenarios is worst-case analysis most critical, and why is it the default in academic algorithm analysis?

---

Worst-case analysis is critical when:
- Response time limits must be guaranteed
- System failures have serious consequences (nuclear plants, medical devices, aircraft control)
- Real-time systems where missing deadlines is unacceptable
- Security systems where worst-case attacks must be defended against

It is the default in academic analysis because:
- It provides guaranteed upper bounds
- It is easier to compute than average case
- It avoids assumptions about input distributions
- It ensures the algorithm will never perform worse than the stated bound

