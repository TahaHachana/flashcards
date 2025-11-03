## Elision Decision Tree Step 1

In the elision decision tree, what's the first question to ask about a function signature?

---

"Does the function signature have reference inputs?" If NO, no lifetimes are needed. If YES, proceed to check if it returns references. This is the foundation of the decision tree because lifetimes only matter when references are involved.

