## Why Substitutions Need Caution

Why is it important to be careful with global substitutions?

---

A single command can rewrite the whole file and what you get is not always what you expect. For example, `:%s/child/children/g` accidentally turns "childish" into "childrenish." Safety habits keep such mistakes recoverable.

